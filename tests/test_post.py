import json
import requests
from jsonschema import validate

from resource import path


def test_create_new_user():
    response = requests.post(
        url="https://reqres.in/api/users", data={"name": "pavel", "job": "builder"}
    )
    body = response.json()
    schema = path('post_method.json')

    assert response.status_code == 201
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
