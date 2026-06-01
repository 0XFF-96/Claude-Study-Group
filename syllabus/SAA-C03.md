# AWS Solutions Architect – Associate (SAA-C03) Syllabus

Authoritative topic checklist for the group. Your personal `members/<you>/progress.md`
is a copy of the four domain sections below — tick boxes there as you learn.

> The `## Domain N` headers and `- [ ]` checkboxes are parsed by `scripts/update_progress.py`.
> Keep the header format intact in your `progress.md`.

Official exam guide: https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf

---

## Domain 1: Design Secure Architectures (30%)

- [ ] IAM: users, groups, roles, policies (identity vs resource policies)
- [ ] IAM best practices: least privilege, MFA, roles over long-lived keys
- [ ] AWS Organizations & Service Control Policies (SCPs)
- [ ] VPC security: security groups vs network ACLs
- [ ] Encryption at rest: KMS, customer vs AWS-managed keys, envelope encryption
- [ ] Encryption in transit: TLS, ACM certificates
- [ ] S3 access control: bucket policies, ACLs, Block Public Access, presigned URLs
- [ ] Secrets management: Secrets Manager vs SSM Parameter Store
- [ ] Edge protection: WAF, Shield, CloudFront security
- [ ] Federated & app identity: IAM Identity Center, Cognito user/identity pools
- [ ] Logging & audit: CloudTrail, GuardDuty, Config

## Domain 2: Design Resilient Architectures (26%)

- [ ] Multi-AZ vs Multi-Region design
- [ ] Auto Scaling groups: policies, lifecycle, warm pools
- [ ] Elastic Load Balancing: ALB vs NLB vs GWLB, target groups, health checks
- [ ] Route 53: routing policies (failover, latency, weighted), health checks
- [ ] Decoupling: SQS (standard vs FIFO), SNS, EventBridge
- [ ] RDS resiliency: Multi-AZ, read replicas, automated backups
- [ ] DynamoDB: global tables, on-demand vs provisioned, DAX
- [ ] S3 durability & versioning, cross-region replication
- [ ] Backup & DR strategies: RPO/RTO, backup/pilot-light/warm-standby/multi-site
- [ ] Storage resiliency: EBS snapshots, EFS, FSx

## Domain 3: Design High-Performing Architectures (24%)

- [ ] Compute selection: EC2 families, Lambda, Fargate, when to use each
- [ ] EC2 sizing: instance types, placement groups
- [ ] Storage performance: EBS volume types (gp3/io2), instance store, EFS modes
- [ ] Caching: ElastiCache (Redis/Memcached), CloudFront, DAX
- [ ] Database scaling: read replicas, Aurora, sharding, RDS Proxy
- [ ] Content delivery & acceleration: CloudFront, S3 Transfer Acceleration, Global Accelerator
- [ ] Data ingestion & streaming: Kinesis (Data Streams/Firehose), MSK
- [ ] Scalable storage: S3 performance, partitioning, multipart upload
- [ ] Networking performance: enhanced networking, VPC endpoints, Direct Connect vs VPN
- [ ] Serverless & event-driven scaling patterns

## Domain 4: Design Cost-Optimized Architectures (20%)

- [ ] EC2 pricing models: On-Demand, Reserved, Savings Plans, Spot
- [ ] Right-sizing compute & Compute Optimizer
- [ ] S3 storage classes & lifecycle policies, Intelligent-Tiering
- [ ] EBS/EFS cost optimization, snapshot management
- [ ] Data transfer cost awareness (egress, cross-AZ, NAT gateway)
- [ ] Serverless for cost: Lambda, Fargate vs always-on EC2
- [ ] Cost visibility: Cost Explorer, Budgets, Cost & Usage Report
- [ ] Trusted Advisor cost checks
- [ ] Decoupled/managed services to reduce ops cost
