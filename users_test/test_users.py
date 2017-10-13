import unittest
from project.users import get_users

class BasicTests(unittest.TestCase):
    def test_request_response(self):
        """ Send a request to the API server to retrieve users."""
        response = get_users()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
