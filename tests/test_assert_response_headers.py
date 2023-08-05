import requests
BASE_URL= "https://reqres.in/"


def test_validate_headers():
 response = requests.get(BASE_URL + "api/users?page=2")
 content_type = response.headers.get("Content-Type")
 assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type
