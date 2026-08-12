import unittest
from unittest.mock import Mock, patch
import requests
from api_client import APIError, fetch_users, normalize_users, search_user, validate_user

VALID_USER = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "leanne@example.com",
}


class TestAPIClient(unittest.TestCase):
    def test_validate_valid_user(self):
        self.assertTrue(validate_user(VALID_USER))

    def test_validate_invalid_user(self):
        self.assertFalse(validate_user({"id": "1"}))

    def test_normalize_users(self):
        data = [VALID_USER, {"id": 2, "name": "Valid", "username": "valid",
                             "email": "valid@example.com"}, {"id": "bad"}]
        self.assertEqual(len(normalize_users(data)), 2)

    def test_search_user(self):
        self.assertEqual(search_user([VALID_USER], 1), VALID_USER)

    def test_search_missing_user(self):
        self.assertIsNone(search_user([VALID_USER], 99))

    @patch("api_client.requests.get")
    def test_fetch_users_success(self, mock_get):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = [VALID_USER]
        mock_get.return_value = response
        self.assertEqual(fetch_users(), [VALID_USER])

    @patch("api_client.requests.get")
    def test_fetch_users_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        with self.assertRaises(APIError):
            fetch_users()

    @patch("api_client.requests.get")
    def test_fetch_users_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(APIError):
            fetch_users()

    @patch("api_client.requests.get")
    def test_fetch_invalid_json(self, mock_get):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.side_effect = ValueError
        mock_get.return_value = response
        with self.assertRaises(APIError):
            fetch_users()


if __name__ == "__main__":
    unittest.main()
