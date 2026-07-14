import pytest

from api.APIClient import APIClient
from helpers.helpers import assert_json_response, load_test_expected, load_test_input


@pytest.fixture(scope="module")
def client():
    return APIClient()


def test_get_users_returns_200_and_expected_structure(client):
    test_name = "test_get_users_returns_200_and_expected_structure"
    input_data = load_test_input("users", test_name)
    response = client.get(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("users", test_name))


def test_post_users_returns_201_and_expected_structure(client):
    test_name = "test_post_users_returns_201_and_expected_structure"
    input_data = load_test_input("users", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("users", test_name))


def test_put_users_returns_200_and_expected_structure(client):
    test_name = "test_put_users_returns_200_and_expected_structure"
    input_data = load_test_input("users", test_name)
    response = client.put(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("users", test_name))


def test_patch_users_returns_200_and_expected_structure(client):
    test_name = "test_patch_users_returns_200_and_expected_structure"
    input_data = load_test_input("users", test_name)
    response = client.patch(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("users", test_name))


def test_delete_users_returns_200_and_expected_structure(client):
    test_name = "test_delete_users_returns_200_and_expected_structure"
    input_data = load_test_input("users", test_name)
    response = client.delete(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("users", test_name))
