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

# Plain-text checkbox (no markdown link) under a domain with no other boxes,
# to exercise the _clean_label fallback and the empty-domain skip in render.
SAMPLE_PLAIN = """# My progress

## Domain 1: Agentic
- [x] Raw topic name

## Domain 2: Tools
"""


def test_parse_breakdown_returns_labels_and_state(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    assert bd["D1 Agentic"] == [("1.1 Agentic loops", True), ("1.2 Multi-agent orchestration", False)]
    assert bd["D2 Tools/MCP"] == [("2.1 Tool interface design", True)]


def test_parse_breakdown_plain_label_fallback(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE_PLAIN, encoding="utf-8")
    bd = up.parse_breakdown(p)
    assert bd["D1 Agentic"] == [("Raw topic name", True)]
    assert bd["D2 Tools/MCP"] == []  # header present, no checkboxes


def test_render_breakdown_has_details_and_marks(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    out = up.render_breakdown("jimmyli", bd)
    assert "<details>" in out
    assert "✅ 1.1 Agentic loops" in out
    assert "⬜ 1.2 Multi-agent orchestration" in out
    assert "✅ 2.1 Tool interface design" in out


def test_render_breakdown_summary_and_domain_pcts(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    out = up.render_breakdown("jimmyli", bd)
    # 2 of 3 boxes done overall -> 67%; D1 1/2 -> 50%; D2 1/1 -> 100%
    assert "67% overall (2/3 subdomains)" in out
    assert "(50%)" in out
    assert "(100%)" in out


def test_render_breakdown_skips_empty_domain(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE_PLAIN, encoding="utf-8")
    bd = up.parse_breakdown(p)
    out = up.render_breakdown("jimmyli", bd)
    # Domain 2 has a header but no boxes -> its block is omitted entirely.
    assert "D2 Tools/MCP" not in out
    assert "✅ Raw topic name" in out


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
