import requests

BASE_URL= "https://reqres.in/"

def test_validate_statuscode():

 response = requests.get(BASE_URL + "api/users?page=2")
 assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

def test_invalid_url_statuscode():
    # Negative test case for invalid URL
    invalid_response = requests.get(BASE_URL + "1/nonexistent")  # Using an invalid URL
    assert invalid_response.status_code == 404, "Expected a 404 status code, but got: " + str(invalid_response.status_code)

