<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![VertexAI](https://img.shields.io/badge/vertexai-v115-green?logo=google%20cloud)](https://cloud.google.com/vertex-ai)
[![Python](https://img.shields.io/badge/Python-3.11.X-blue.svg?logo=python)](https://www.python.org/)
[![git](https://img.shields.io/badge/git-v2.39.X-red.svg?logo=git)](https://git-scm.com/)

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/davivienda-colombia/davi-coe-terraform-test-lib">
    <img src="./utils/davi_logo.png" alt="Logo" width="550">
  </a>
</div>

<br />
<div align="center">
  <a href="https://github.com/davivienda-colombia/davi-coe-google-cloud">
    <img src="./utils/gcp_logo.png" alt="Logo" width="190" height="70">
  </a>
  <p align="center">
    Client component which predicts the infrastructure required by a functional domain for Davivienda.
    <br />
    <a href="https://github.com/davivienda-colombia/davi-coe-aws-s3-iac/issues">Report Bug</a>
    ·
    <a href="https://github.com/davivienda-colombia/davi-coe-aws-s3-iac/issues">Request Feature</a>
  </p>
</div>

### VertexAI Documentation

Explore the comprehensive documentation on Google Cloud Vertex AI service at the official reference of Google Cloud.

[![Click here to read](https://img.shields.io/badge/Click_here_to_read-blue?style=plastic&labelColor=white&color=blue&logoWidth=20&logo=GoogleCloud&logoColor=blue)](https://cloud.google.com/vertex-ai)

## Usage

### Send a post with the parameters that describe the architecture.

```json
POST /echo/post/json HTTP/1.1
Host: https://container-ai-arch-lzmkizmaoq-uc.a.run.app
Accept: application/json
Content-Type: application/json
{
    "Deployment Platform": "Containers",
    "Networking": "Connecting GCP and Onpremise",
    "Database": "NoSQL Database",
    "Security Protection": "DDOS protection and WAF",
    "DevOps": "Deploying IaC",
    "Logging": "Analyzing an error",
    "Monitoring": "Creating alerts"
}
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Inputs

| Name                | Version                                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Deployment Platform | <ul><li>Mobile Backend</li> <li>Event driven</li><li>Web Applications</li><li>Containers</li></ul>                                              |
| Networking          | <ul><li>Connecting GCP and Onpremise</li> <li>Connecting to WS* and APIs</li><li>Connecting the Sites</li><li>Connecting to CDN Providers</li></ul> |
| Database            | <ul><li>Relational Database</li> <li>NoSQL Database</li></ul>                                                                                   |
| Security Protection | <ul><li>Authentication Mechanism</li> <li>DDOS protection and WAF.</li><li>Secure Secret Storage API</li><li>Reverse proxy to access VMs</li></ul> |
| DevOps              | <ul><li>Repository</li><li>Deployment</li><li>Artifact</li><li>Fourth item</li></ul>                                                            |
| Logging             | <ul><li>Logging</li></ul>                                                                                                                       |
| Monitoring          | <ul><li>Basic</li><li>APM</li></ul>                                                                                |


## Outputs

| Name                | Version                                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Deployment Platform | <ul>Firebase<li></li><li>Cloud Functions</li><li>App Engine</li><li>Cloud Run</li><li>Kubernetes Engine</li></ul>                                 |
| Networking          | <ul><li>VPN/HVPN</li><li>Interconnect</li><li>Cloud Router</li><li>Peering</li><li>Network Connectivity Center</li><li>CDN Interconnect</li></ul> |
| Database            | <ul><li>Cloud SQL</li><li>AlloyDB</li><li>Cloud Spanner</li><li>Firestore</li><li>Bigtable</li></ul>                                              |
| Security Protection | <ul><li>Authentication and Authorization</li><li>Secret Manager</li><li>Identity Award Proxy</li><li>Cloud Armor</li><li>VPC Service Controls</li></ul>               |
| DevOps              | <ul><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ul>                                                           |
| Logging             | <ul><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ul>                                                           |
| Monitoring          | <ul><li>First item</li><li>Second item</li><li>Third item</li><li>Fourth item</li></ul>                                                           |

## Additional Documentation
The next Figure illustrates the architecture of the [Framework AI Cloud Architecture](./utils/framework-logo.png)

## Mantainers
Module is maintained by [COE Arquitectura Cloud](https://github.com/orgs/davivienda-colombia/teams/coe-team)

### Authors
-  Yury Niño Roa [yurynino_davicode](https://github.com/yurynino_davicode)


Please add here if you made a contribution

<div align="right">

[![Back to Top](https://img.shields.io/badge/%E2%96%B2%EF%B8%8F-Back_to_Top-238636?style=plastic&labelColor=white&color=238636&logo=none&logoColor=white&labelBorderRadius=8)](#Top)

</div>
