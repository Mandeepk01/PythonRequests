import unittest
import requests
BASE_URL= "https://reqres.in/"

class APITestCase(unittest.TestCase):
    def test_status_code(self):
        response = requests.get(BASE_URL + "api/users?page=2")
        self.assertEqual(response.status_code, 200, "Unexpected status code")

if __name__ == "__main__":
    unittest.main()