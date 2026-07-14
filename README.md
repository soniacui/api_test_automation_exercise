# api_test_automation_exercise

Simple API test automation framework using Python and pytest.

## Project structure

- `api/client.py`: Reusable API client to call endpoints.
- `tests/conftest.py`: Shared pytest fixtures.
- `tests/test_todos.py`: Happy path test for `/todos/1`.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```