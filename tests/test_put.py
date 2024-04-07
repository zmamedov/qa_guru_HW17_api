import json
import requests
from jsonschema import validate

from resource import path


def test_update_user_job():
    new_user_id = requests.post(
        url="https://reqres.in/api/users/", data={"name": "Ivan", "job": "driver"}
    ).json()['id']

    response = requests.put(
        url=f"https://reqres.in/api/users/{new_user_id}", data={"name": "Ivan", "job": "driver"}
    )
    body = response.json()
    schema = path('put_method.json')

    assert response.status_code == 200
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
