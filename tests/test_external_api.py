import json
import unittest
from unittest.mock import MagicMock, Mock, patch
from src.external_api import convert_to


class TestConvertTo(unittest.TestCase):
    @patch("requests.request")
    def test_convert_to_success(self, mock_request: MagicMock) -> None:
        """Mock для успешного ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({"info": {"rate": 75.0}})
        mock_request.return_value = mock_response
        result = convert_to(100, "USD", "RUB")
        self.assertEqual(result, 75.0)

    @patch("requests.request")
    def test_convert_to_failure(self, mock_request: MagicMock) -> None:
        """Mock для неудачного ответа"""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.reason = "Bad Request"
        mock_request.return_value = mock_response
        result = convert_to(100, "USD", "RUB")
        self.assertEqual(result, "Bad Request")
