import requests
BASE_URL= "https://reqres.in/"

def test_handle_exception():
 try:
    response = requests.get(BASE_URL + "api/users?page=2")
    response.raise_for_status()
    print("Request successful")
 except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))
