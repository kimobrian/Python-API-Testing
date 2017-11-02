import unittest
from users import get_users, get_user
from unittest.mock import patch, Mock

class BasicTests(unittest.TestCase):
    def test_request_response(self):
        mock_get_patcher = patch('users.requests.get')
        users = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200.
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = users

        # Call the service, which will send a request to the server.
        response = get_users()

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), users)

    @patch('users.get_users')
    def test_get_one_user(self, mock_get_users):
        """Test for getting one user using their userID"""
        users = [
            {'phone': '514-794-6957', 'first_name': 'Brant', 'last_name': 'Mekhi', 'id': 0},
            {'phone': '772-370-0117', 'first_name': 'Thalia', 'last_name': 'Kenyatta', 'id': 1},
            {'phone': '176-290-7637', 'first_name': 'Destin', 'last_name': 'Soledad', 'id': 2}
            ]
        mock_get_users.return_value = Mock()
        mock_get_users.return_value.json.return_value = users
        user = get_user(2)
        self.assertEqual(user, users[2])

if __name__ == "__main__":
    unittest.main()
