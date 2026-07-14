import pytest

from api.APIClient import APIClient
from helpers.helpers import assert_json_response, load_test_expected, load_test_input


@pytest.fixture(scope="module")
def client():
    return APIClient()


def test_get_albums_returns_200_retrieves_resource(client):
    test_name = "test_get_albums_returns_200_retrieves_resource"
    input_data = load_test_input("albums", test_name)
    response = client.get(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("albums", test_name))


def test_post_albums_returns_201_creates_resource(client):
    test_name = "test_post_albums_returns_201_creates_resource"
    input_data = load_test_input("albums", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("albums", test_name))


def test_put_albums_returns_200_updates_resource(client):
    test_name = "test_put_albums_returns_200_updates_resource"
    input_data = load_test_input("albums", test_name)
    response = client.put(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("albums", test_name))


def test_patch_albums_returns_200_updates_partial_resource(client):
    test_name = "test_patch_albums_returns_200_updates_partial_resource"
    input_data = load_test_input("albums", test_name)
    response = client.patch(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("albums", test_name))


def test_delete_albums_returns_200_deletes_resource(client):
    test_name = "test_delete_albums_returns_200_deletes_resource"
    input_data = load_test_input("albums", test_name)
    response = client.delete(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("albums", test_name))


def test_post_albums_returns_201_with_null_values(client):
    test_name = "test_post_albums_returns_201_with_null_values"
    input_data = load_test_input("albums", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("albums", test_name))


def test_post_albums_returns_201_with_missing_payload_fields(client):
    test_name = "test_post_albums_returns_201_with_missing_payload_fields"
    input_data = load_test_input("albums", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("albums", test_name))


def test_post_albums_returns_201_with_long_string_payload(client):
    test_name = "test_post_albums_returns_201_with_long_string_payload"
    input_data = load_test_input("albums", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("albums", test_name))


def test_post_albums_returns_201_with_special_characters(client):
    test_name = "test_post_albums_returns_201_with_special_characters"
    input_data = load_test_input("albums", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("albums", test_name))
