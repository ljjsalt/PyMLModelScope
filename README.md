# MLModelScope

Migarte from Go to Python

## Roles and its implementation

- Server - FastAPI & gPPC client
- Agent - ray instance (grpc server)
- Client - HTTP Requests

## Project Management

- pre-commit
  - mypy
<!-- - pylint when necessary
- pytest when necessary
- CI when necessary -->
<!-- - pybind (C++11) performance -->

## Document

- Read the Docs

## models

- Resources
  - [Pytorch](https://pytorch.org/vision/stable/models.html)
  - [Hugging Face](https://huggingface.co/models)
  - [Tensorflow Hub](https://tfhub.dev/)

## dataset

- S3 object storage
  - S3 Plugin (PyTorch)

- Resources
  - [Hugging Face](https://huggingface.co/docs/datasets/index)
  - [Registry of Open Data on AWS](https://registry.opendata.aws/)
  - [Torchvision.datasets](https://pytorch.org/vision/stable/datasets.html)
  - [TensorFlow Datasets](https://www.tensorflow.org/datasets)

- `ray.data`
  - `Datasets` reading from a file-based datasource (e.g., S3)
  - `Pipelines` executing data transformations(preprocessing) synchronously in blocking calls (overlap dataset computations with output).
