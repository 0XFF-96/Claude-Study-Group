"""Tests for update_progress subdomain breakdown. Run: python3 tests/test_update_progress.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import update_progress as up  # noqa: E402

SAMPLE = """# My progress

## Domain 1: Agentic
- [x] [1.1 Agentic loops](../../syllabus/domains/domain-1-agentic.md#11-agentic-loops)
- [ ] [1.2 Multi-agent orchestration](../../syllabus/domains/domain-1-agentic.md#12-multi-agent-orchestration)

## Domain 2: Tools
- [x] [2.1 Tool interface design](../../syllabus/domains/domain-2-tools-mcp.md#21-tool-interface-design)
"""


def test_parse_breakdown_returns_labels_and_state(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    assert bd["D1 Agentic"] == [("1.1 Agentic loops", True), ("1.2 Multi-agent orchestration", False)]
    assert bd["D2 Tools/MCP"] == [("2.1 Tool interface design", True)]


def test_render_breakdown_has_details_and_marks(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    out = up.render_breakdown("jimmyli", bd)
    assert "<details>" in out
    assert "✅ 1.1 Agentic loops" in out
    assert "⬜ 1.2 Multi-agent orchestration" in out
    assert "✅ 2.1 Tool interface design" in out


def _run():
    import tempfile
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            with tempfile.TemporaryDirectory() as d:
                try:
                    fn(Path(d))
                    print(f"PASS {name}")
                except AssertionError as e:
                    failures += 1
                    print(f"FAIL {name}: {e}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_run())
