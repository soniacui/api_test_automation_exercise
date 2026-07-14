import pytest
from api.APIClient import APIClient


@pytest.fixture
def client():
    return APIClient()


def assert_json_response(response, expected_status, expected_id=None, expected_title=None):
    assert response.status_code == expected_status
    assert response.headers["content-type"].startswith("application/json")

    data = response.json()
    assert isinstance(data, dict)

    if expected_id is not None:
        assert data["id"] == expected_id

    if expected_title is not None:
        assert "title" in data
        assert isinstance(data["title"], str)
        assert data["title"] == expected_title


def test_get_todos_returns_200_and_expected_structure(client):
    response = client.get("/todos/1")

    assert_json_response(response, 200, expected_id=1, expected_title="delectus aut autem")


def test_get_posts_returns_200_and_expected_structure(client):
    response = client.get("/posts/1")

    assert_json_response(response, 200, expected_id=1, expected_title="sunt aut facere repellat provident occaecati excepturi optio reprehenderit")


def test_post_posts_creates_new_resource(client):
    payload = {
        "title": "New post",
        "body": "This is a test body",
        "userId": 1,
    }
    response = client.post("/posts", json=payload)

    assert_json_response(response, 201, expected_id=101)
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]


def test_put_posts_updates_entire_resource(client):
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1,
    }
    response = client.put("/posts/1", json=payload)

    assert_json_response(response, 200, expected_id=1)
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]


def test_patch_posts_updates_partial_resource(client):
    payload = {"title": "Patched title"}
    response = client.patch("/posts/1", json=payload)

    assert_json_response(response, 200, expected_id=1)
    assert response.json()["title"] == payload["title"]


def test_delete_posts_removes_resource(client):
    response = client.delete("/posts/1")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert isinstance(response.json(), dict)
    assert response.json() == {}