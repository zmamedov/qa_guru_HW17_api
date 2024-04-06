import json
import requests
from jsonschema import validate


def test_create_new_user():
    response = requests.post(
        url="https://reqres.in/api/users", data={"name": "pavel", "job": "builder"}
    )
    body = response.json()

    assert response.status_code == 201
    with open('../json_schemas/post_method.json') as file:
        f = file.read()
        validate(body, schema=json.loads(f))
