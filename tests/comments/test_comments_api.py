import pytest

from api.APIClient import APIClient
from helpers.helpers import assert_json_response, load_test_expected, load_test_input


@pytest.fixture(scope="module")
def client():
    return APIClient()


def test_get_comments_returns_200_retrieves_resource(client):
    test_name = "test_get_comments_returns_200_retrieves_resource"
    input_data = load_test_input("comments", test_name)
    response = client.get(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("comments", test_name))


def test_post_comments_returns_201_creates_resource(client):
    test_name = "test_post_comments_returns_201_creates_resource"
    input_data = load_test_input("comments", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("comments", test_name))


def test_put_comments_returns_200_updates_resource(client):
    test_name = "test_put_comments_returns_200_updates_resource"
    input_data = load_test_input("comments", test_name)
    response = client.put(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("comments", test_name))


def test_patch_comments_returns_200_updates_partial_resource(client):
    test_name = "test_patch_comments_returns_200_updates_partial_resource"
    input_data = load_test_input("comments", test_name)
    response = client.patch(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 200, load_test_expected("comments", test_name))


def test_delete_comments_returns_200_deletes_resource(client):
    test_name = "test_delete_comments_returns_200_deletes_resource"
    input_data = load_test_input("comments", test_name)
    response = client.delete(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("comments", test_name))


def test_get_comments_returns_200_and_id_is_not_unexpected(client):
    test_name = "test_get_comments_returns_200_and_id_is_not_unexpected"
    input_data = load_test_input("comments", test_name)
    response = client.get(input_data["endpoint"])
    assert_json_response(response, 200, load_test_expected("comments", test_name))
    assert response.json()["id"] != input_data["unexpected_id"]


def test_post_comments_returns_201_with_missing_payload_fields(client):
    test_name = "test_post_comments_returns_201_with_missing_payload_fields"
    input_data = load_test_input("comments", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("comments", test_name))


def test_post_comments_returns_201_with_special_characters(client):
    test_name = "test_post_comments_returns_201_with_special_characters"
    input_data = load_test_input("comments", test_name)
    response = client.post(input_data["endpoint"], json=input_data["payload"])
    assert_json_response(response, 201, load_test_expected("comments", test_name))


def test_get_comments_returns_404_for_non_existent_route(client):
    test_name = "test_get_comments_returns_404_for_non_existent_route"
    input_data = load_test_input("comments", test_name)
    response = client.get(input_data["endpoint"])
    assert_json_response(response, 404, load_test_expected("comments", test_name))
