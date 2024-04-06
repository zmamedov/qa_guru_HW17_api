import requests


def test_delete_user():
    new_user_id = requests.post(
        url="https://reqres.in/api/users/", data={"name": "John", "job": "officer"}
    ).json()['id']

    response = requests.delete(url=f"https://reqres.in/api/users/{new_user_id}")

    assert response.status_code == 204
