# login_helper.py
import requests
import allure

BASE_URL = "http://172.25.185.68:1337"
LOGIN_ENDPOINT = "/api/auth/local"
GRAPHQL_ENDPOINT = "http://172.25.185.68:10104/graphql"
jwt_token = None

def login():
    global jwt_token
    login_payload = {
        "identifier": "vanthuancontact@gmail.com",
        "password": "Kentran212431302&"
    }
    login_response = requests.post(BASE_URL + LOGIN_ENDPOINT, json=login_payload)
    login_data = login_response.json()
    jwt_token = login_data.get("jwt")
    print(f"jwt: {jwt_token}")
    allure.attach(jwt_token, name="JWT Token", attachment_type=allure.attachment_type.TEXT)
    assert jwt_token is not None, "Login failed"
    return jwt_token
