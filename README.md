<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![VertexAI](https://img.shields.io/badge/vertexai-v115-green?logo=google%20cloud)](https://cloud.google.com/vertex-ai)
[![Python](https://img.shields.io/badge/Python-3.11.X-blue.svg?logo=python)](https://www.python.org/)
[![git](https://img.shields.io/badge/git-v2.39.X-red.svg?logo=git)](https://git-scm.com/)

<!-- PROJECT LOGO -->

<br />
<div align="center">
    <img src="./utils-adiutor/logo-adiutor.png" alt="Logo" width="550">
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
    "architecture-picture": "",
}
```

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Inputs

| Name       | Type   | Description                                                |
|------------|--------|------------------------------------------------------------|
| project_id | String | Name of the Google Cloud project in which you use VertexAI | 
| region     | String | Name of the Google Cloud region in which you use VertexAI  | 
| picture    | String | URL where you can find the architecture picture            | 


## Outputs

| Name                | Description                                                    |
|---------------------|----------------------------------------------------------------|
| gcloud-commands     | The gcloud list commands to implement the architecture picture |

### Authors
-  Yury Niño Roa [yurynino](https://github.com/yurynino)

Please add here if you made a contribution

<div align="right">

[![Back to Top](https://img.shields.io/badge/%E2%96%B2%EF%B8%8F-Back_to_Top-238636?style=plastic&labelColor=white&color=238636&logo=none&logoColor=white&labelBorderRadius=8)](#Top)

</div>
