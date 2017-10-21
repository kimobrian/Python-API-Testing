import unittest
from project.users import get_users
from unittest.mock import patch

class BasicTests(unittest.TestCase):
    def test_request_response(self):
        with patch('project.users.requests.get') as mock_get:
            # Configure the mock to return a response with status code 200.
            mock_get.return_value.status_code = 200

            # Call the function, which will send a request to the server.
            response = get_users()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
