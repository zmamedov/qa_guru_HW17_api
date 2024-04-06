import json
import requests
from jsonschema import validate


def test_return_single_user():
    response = requests.get(
        url="https://reqres.in/api/users/3"
    )
    body = response.json()

    assert response.status_code == 200
    with open('../json_schemas/get_method.json') as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_return_nonexistent_user():
    response = requests.get(
        url="https://reqres.in/api/users/233"
    )

    assert response.status_code == 404
    assert response.json() == {}
