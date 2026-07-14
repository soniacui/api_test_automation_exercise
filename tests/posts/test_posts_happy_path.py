import pytest

from api.APIClient import APIClient
from tests.fixture_loader import load_test_expected, load_test_input


@pytest.fixture(scope="module")
def client():
    return APIClient()


def test_get_posts_returns_200_and_expected_structure(client):
    test_name = "test_get_posts_returns_200_and_expected_structure"
    input_data = load_test_input("posts", test_name)
    response = client.get(input_data["endpoint"])
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == load_test_expected("posts", test_name)


def test_post_posts_returns_201_and_expected_structure(client):
    test_name = "test_post_posts_returns_201_and_expected_structure"
    input_data = load_test_input("posts", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert response.status_code == 201
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == load_test_expected("posts", test_name)


def test_put_posts_returns_200_and_expected_structure(client):
    test_name = "test_put_posts_returns_200_and_expected_structure"
    input_data = load_test_input("posts", test_name)
    response = client.put(input_data["endpoint"], json=input_data["payload"])
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == load_test_expected("posts", test_name)


def test_patch_posts_returns_200_and_expected_structure(client):
    test_name = "test_patch_posts_returns_200_and_expected_structure"
    input_data = load_test_input("posts", test_name)
    response = client.patch(input_data["endpoint"], json=input_data["payload"])
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == load_test_expected("posts", test_name)


def test_delete_posts_returns_200_and_expected_structure(client):
    test_name = "test_delete_posts_returns_200_and_expected_structure"
    input_data = load_test_input("posts", test_name)
    response = client.delete(input_data["endpoint"])
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == load_test_expected("posts", test_name)
