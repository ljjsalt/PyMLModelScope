# MLModelScope

Migarte from Go to Python

## Project Management

- pre-commit
- pylint
- pytest
- CI
- mypy static type checker
<!-- - pybind (C++11) performance -->

## Document

- Read the Docs

## dataset

- S3 object storage
  - S3 Plugin (PyTorch)

- `ray.data`
  - `Datasets` reading from a file-based datasource (e.g., S3)
  - `Pipelines` executing data transformations(preprocessing) synchronously in blocking calls (overlap dataset computations with output).
