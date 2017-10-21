import unittest
from project.users import get_users
from unittest.mock import patch

class BasicTests(unittest.TestCase):
    def test_request_response(self):
        mock_get_patcher = patch('project.users.requests.get')

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200.
        mock_get.return_value.status_code = 200

        # Call the service, which will send a request to the server.
        response = get_users()

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
