import unittest
from project.users import get_users
from unittest.mock import patch

class BasicTests(unittest.TestCase):
    @patch('project.users.requests.get')  # Mock 'requests' module 'get' method.
    def test_request_response(self, mock_get):
        """ Send a request to the API server to retrieve users."""
        mock_get.return_value.status_code = 200 # Mock status code of response.
        response = get_users()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
