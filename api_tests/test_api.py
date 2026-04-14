import pytest
import time
import requests

user_data = [
    {"name": "morpheus", "job": "leader"},
    {"name": "viktoria", "job": "automation_engineer"}
]

BASE_URL = "https://reqres.in/api"


def check_response(response, expected_status):
    if response.status_code in [401, 403, 429]:
        pytest.skip(f"Server returned {response.status_code}. Anti-bot protection is active.")
    assert response.status_code == expected_status


@pytest.mark.parametrize("user", user_data)
def test_create_user(user):
    """Test Case 2: POST - Create User"""
    response = requests.post(f"{BASE_URL}/users", json=user)
    check_response(response, 201)

    res_body = response.json()
    assert res_body["name"] == user["name"]


def test_list_users():
    """Test Case 1: GET - List Users"""
    response = requests.get(f"{BASE_URL}/users?page=2")
    check_response(response, 200)

    data = response.json()
    users = data["data"]
    assert users[0]["last_name"] == "Lawson"
    assert len(users) <= data["total"]