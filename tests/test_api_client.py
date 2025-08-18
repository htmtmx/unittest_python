import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    @patch('src/api_client.request.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code=200
        mock_get.return_value.json.return_value = {
            'countryName': 'United States', 
            'regionName': 'California',
            'capital': 'Washington D.C.', 
            'cityName': 'Mountain View',
        }
        data_expected = {'countryName': 'United States', 'regionName': 'California',
                         'capital': 'Washington D.C.', 'cityName': 'Mountain View'}
        data_actual = get_location(ip='8.8.8.8')
        self.assertEqual(data_actual, data_expected)
