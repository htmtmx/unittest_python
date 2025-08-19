import unittest
from unittest.mock import patch

from src.api_client import get_location


class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "United States",
            "regionName": "California",
            "capital": "Washington D.C.",
            "cityName": "Mountain View",
            "countryCode": "US",
        }
        result = get_location(ip="8.8.8.8", country_code="US")
        self.assertEqual(result.get("country"), "United States")
        self.assertEqual(result.get("region"), "California")
        self.assertEqual(result.get("capital"), "Washington D.C.")
        self.assertEqual(result.get("city"), "Mountain View")
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_country_code(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "United States",
            "regionName": "California",
            "capital": "Washington D.C.",
            "cityName": "Mountain View",
            "countryCode": "US",
        }
        country_code = "US"
        result = get_location(ip="8.8.8.8", country_code=country_code)
        self.assertEqual(result.get("country_code"), country_code)
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
