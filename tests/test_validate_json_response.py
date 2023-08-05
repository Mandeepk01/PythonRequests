import requests

BASE_URL = "https://reqres.in/"

def test_validate_json():
    response = requests.get(BASE_URL + "api/users?page=2")
    data = response.json()

    # Check if the response data is a dictionary
    assert isinstance(data, dict), "Response data is not a dictionary"

    # Check if the "per_page" key is present in the JSON response
    assert "per_page" in data, "Expected 'per_page' key not found in the JSON response"

    # Check if the value of the "per_page" key is an integer
    assert isinstance(data["per_page"], int), "'per_page' value is not an integer"

    # Check if the "data" key is present in the JSON response
    assert "data" in data, "Expected 'data' key not found in the JSON response"

    # Check if the value of the "data" key is a list
    assert isinstance(data["data"], list), "'data' value is not a list"

    # Check if the "data" list is not empty
    assert len(data["data"]) > 0, "'data' list is empty"

    # Check if each item in the "data" list is a dictionary
    for item in data["data"]:
        assert isinstance(item, dict), "Item in 'data' list is not a dictionary"
