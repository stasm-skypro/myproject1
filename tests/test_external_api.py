import json
import unittest
from unittest.mock import Mock, patch

from src.external_api import _convert_to


class TestConvertTo(unittest.TestCase):
    @patch("requests.request")
    def test_requests_success1(self, mock_request: Mock) -> None:
        """Mock для успешного ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({"info": {"rate": 1.0}})
        mock_request.return_value = mock_response
        result = _convert_to(1, "USD", "RUB")
        self.assertEqual(result, 1.0)

    @patch("requests.request")
    def test_convert_to_success2(self, mock_request: Mock) -> None:
        """Mock для успешного ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({"info": {"rate": 1.0}})
        mock_request.return_value = mock_response
        result = _convert_to(1, "EUR", "RUB")
        self.assertEqual(result, 1.0)

    @patch("requests.request")
    def test_convert_to_failure(self, mock_request: Mock) -> None:
        """Mock для неудачного ответа"""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.reason = "Bad Request"
        mock_request.return_value = mock_response
        result = _convert_to(1, "USD", "RUB")
        self.assertEqual(result, "Bad Request")


if __name__ == "__main__":
    unittest.main()
