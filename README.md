<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![VertexAI](https://img.shields.io/badge/vertexai-v115-green?logo=google%20cloud)](https://cloud.google.com/vertex-ai)
[![Python](https://img.shields.io/badge/Python-3.11.X-blue.svg?logo=python)](https://www.python.org/)
[![git](https://img.shields.io/badge/git-v2.39.X-red.svg?logo=git)](https://git-scm.com/)

<br />
<div align="center">
    <img src="./utils-adiutor/logo-adiutor.png" alt="Logo" width="100">
</div>

### VertexAI Documentation

Explore the comprehensive documentation on Google Cloud Vertex AI service at the official reference of Google Cloud.

<div align="center">
    [![Click here to read](https://img.shields.io/badge/Click_here_to_read-blue?style=plastic&labelColor=white&color=blue&logoWidth=20&logo=GoogleCloud&logoColor=blue)](https://cloud.google.com/vertex-ai)
</div>

## Inputs

| Name    | Type   | Description                                               |
|---------|--------|-----------------------------------------------------------|
| project | String | ID of the Google Cloud project in which you use VertexAI  | 
| region  | String | Name of the Google Cloud region in which you use VertexAI | 
| picture | String | URL where you can find the architecture picture           |

## Outputs

| Name                | Description                                                    |
|---------------------|----------------------------------------------------------------|
| gcloud-commands     | The gcloud list commands to implement the architecture picture |

## Example
### Send a post with the project ID, the region and the gcs path picture.

```json
POST /echo/post/json HTTP/1.1
Host: https://container-ai-arch-lzmkizmaoq-uc.a.run.app
Accept: application/json
Content-Type: application/json
{
    "project": "",
    "region": "",
    "picture": "",
}
```

### Authors
-  Yury Niño Roa [yurynino](https://github.com/yurynino)