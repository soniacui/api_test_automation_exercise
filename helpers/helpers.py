import json
from pathlib import Path


FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures"


def load_test_input(endpoint: str, test_name: str) -> dict:
    file_name = f"{test_name}_input.json"
    with (FIXTURES_DIR / "input" / endpoint / file_name).open("r", encoding="utf-8") as f:
        return json.load(f)


def load_test_expected(endpoint: str, test_name: str) -> dict:
    file_name = f"{test_name}_expected.json"
    with (FIXTURES_DIR / "expected" / endpoint / file_name).open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_json_response(response, expected_status_code, expected_body):
    assert response.status_code == expected_status_code
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == expected_body
