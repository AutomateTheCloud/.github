<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/atc-lockup-horizontal-dark.svg">
    <img src="assets/atc-lockup-horizontal.svg" alt="Automate the Cloud" width="420">
  </picture>
</p>

<p align="center">
  Cloud computing, taught in the open.<br>
  <a href="https://automatethe.cloud">automatethe.cloud</a>
</p>

---

Automate the Cloud teaches cloud infrastructure in public. Everything we publish here is free to
read, use, and adapt, and keeping it that way is written into our bylaws.

**What we do**

- **Open educational material.** Guides, best practices, and example infrastructure code. The
  modules below are meant to be studied as much as used: each one documents its defaults and why
  they were chosen.
- **Tech help for nonprofits.** Free and below-cost IT help for nonprofits, schools, congregations,
  and community groups that serve the public, including small groups without formal tax-exempt
  status.
- **Scholarships** for students studying technology. The first award cycle is not open yet.

## Terraform modules for AWS

Each module's README covers its inputs, outputs, and examples.

**Networking**

| Module | What it creates |
|---|---|
| [terraform-aws-vpc](https://github.com/AutomateTheCloud/terraform-aws-vpc) | A VPC with private, restricted, and public subnets across three Availability Zones |
| [terraform-aws-vpc_dhcp_options](https://github.com/AutomateTheCloud/terraform-aws-vpc_dhcp_options) | A DHCP option set, with defaults that match the Region's own |
| [terraform-aws-vpc_peering](https://github.com/AutomateTheCloud/terraform-aws-vpc_peering) | A VPC peering connection, accepted and routed across Regions and accounts |
| [terraform-aws-nat_gateway](https://github.com/AutomateTheCloud/terraform-aws-nat_gateway) | Public or private NAT gateways and the routes to them |
| [terraform-aws-eip](https://github.com/AutomateTheCloud/terraform-aws-eip) | An Elastic IP address for use in a VPC |
| [terraform-aws-transit_gateway](https://github.com/AutomateTheCloud/terraform-aws-transit_gateway) | A transit gateway and route table, optionally shared through AWS RAM |
| [terraform-aws-transit_gateway_attachment](https://github.com/AutomateTheCloud/terraform-aws-transit_gateway_attachment) | A VPC attachment to a transit gateway, with routes from the VPC |
| [terraform-aws-security_group](https://github.com/AutomateTheCloud/terraform-aws-security_group) | A security group with inbound and outbound rules |

**DNS and certificates**

| Module | What it creates |
|---|---|
| [terraform-aws-route53_zone](https://github.com/AutomateTheCloud/terraform-aws-route53_zone) | A Route 53 hosted zone, public or private |
| [terraform-aws-route53_resolver_endpoint](https://github.com/AutomateTheCloud/terraform-aws-route53_resolver_endpoint) | A Route 53 Resolver inbound or outbound endpoint |
| [terraform-aws-route53_resolver_rule](https://github.com/AutomateTheCloud/terraform-aws-route53_resolver_rule) | A Route 53 Resolver rule, optionally shared with other accounts |
| [terraform-aws-acm](https://github.com/AutomateTheCloud/terraform-aws-acm) | An ACM certificate validated through Route 53, including across accounts |

**Data and storage**

| Module | What it creates |
|---|---|
| [terraform-aws-rds](https://github.com/AutomateTheCloud/terraform-aws-rds) | An encrypted, private RDS instance with read replicas, logs, and monitoring |
| [terraform-aws-rds_aurora](https://github.com/AutomateTheCloud/terraform-aws-rds_aurora) | An Aurora PostgreSQL or MySQL cluster |
| [terraform-aws-rds_aurora_global_cluster](https://github.com/AutomateTheCloud/terraform-aws-rds_aurora_global_cluster) | An Aurora global cluster, encrypted and protected from deletion |
| [terraform-aws-dynamodb_table](https://github.com/AutomateTheCloud/terraform-aws-dynamodb_table) | A DynamoDB table with indexes, autoscaling, streams, TTL, and replicas |
| [terraform-aws-elasticache_redis](https://github.com/AutomateTheCloud/terraform-aws-elasticache_redis) | An ElastiCache replication group running Redis OSS or Valkey, encrypted and private |
| [terraform-aws-s3_bucket](https://github.com/AutomateTheCloud/terraform-aws-s3_bucket) | S3 buckets that are private, encrypted, and HTTPS-only |
| [terraform-aws-efs](https://github.com/AutomateTheCloud/terraform-aws-efs) | An EFS file system with encryption, TLS, and mount targets |
| [terraform-aws-influx](https://github.com/AutomateTheCloud/terraform-aws-influx) | A Timestream for InfluxDB instance, private and encrypted, with a security group for its clients |
| [terraform-aws-redshift](https://github.com/AutomateTheCloud/terraform-aws-redshift) | A Redshift cluster, encrypted and private, with TLS required and its password in Secrets Manager |
| [terraform-aws-redshift_serverless](https://github.com/AutomateTheCloud/terraform-aws-redshift_serverless) | A Redshift Serverless namespace and workgroup, encrypted and private, with TLS required |

**Security and keys**

| Module | What it creates |
|---|---|
| [terraform-aws-kms_key](https://github.com/AutomateTheCloud/terraform-aws-kms_key) | A KMS key and alias, with a policy for administrators and users |
| [terraform-aws-ssh_key_pair](https://github.com/AutomateTheCloud/terraform-aws-ssh_key_pair) | An EC2 key pair from an SSH public key |

**Delivery and operations**

| Module | What it creates |
|---|---|
| [terraform-aws-ecr](https://github.com/AutomateTheCloud/terraform-aws-ecr) | An ECR repository with lifecycle rules and a repository policy |
| [terraform-aws-ecs_cluster-fargate](https://github.com/AutomateTheCloud/terraform-aws-ecs_cluster-fargate) | An ECS cluster for Fargate tasks, with Container Insights and ECS Exec settings |
| [terraform-aws-instance_deployment-linux](https://github.com/AutomateTheCloud/terraform-aws-instance_deployment-linux) | Linux EC2 instances in an Auto Scaling group, set up at boot and replaced in rolling batches |
| [terraform-aws-codedeploy](https://github.com/AutomateTheCloud/terraform-aws-codedeploy) | A CodeDeploy application and its service role |
| [terraform-aws-sqs](https://github.com/AutomateTheCloud/terraform-aws-sqs) | An SQS queue with an optional dead-letter queue |
| [terraform-aws-ssm_document](https://github.com/AutomateTheCloud/terraform-aws-ssm_document) | A Systems Manager document, such as a Run Command document or Automation runbook |

## Licensing

The modules are open source. Our code is released under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), and each repository's `LICENSE`
file states its terms. The Automate the Cloud name and logo are not covered by these licenses.

---

<sub>Automate the Cloud Inc. is a 501(c)(3) public charity based in Louisville, Kentucky.</sub>
