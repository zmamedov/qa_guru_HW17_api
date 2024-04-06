import json
import requests
from jsonschema import validate

url = "https://reqres.in/api/register"


def test_successful_registration():
    response = requests.post(
        url=url, data={"email": "janet.weaver@reqres.in", "password": "123456"}
    )
    body = response.json()

    assert response.status_code == 200
    with open('../json_schemas/register_user.json') as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_unsuccessful_registration_without_password():
    response = requests.post(
        url=url, data={"email": "janet.weaver@reqres.in"}
    )
    body = response.json()

    assert response.status_code == 400
    with open('../json_schemas/bad_register_user.json') as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_unsuccessful_registration_with_nonexistent_email():
    response = requests.post(
        url=url, data={"email": "jjjj.weaver@reqres.in"}
    )
    body = response.json()

    assert response.status_code == 400
    with open('../json_schemas/bad_register_user.json') as file:
        f = file.read()
        validate(body, schema=json.loads(f))
