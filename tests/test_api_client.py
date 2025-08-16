import unittest
from src.api_client import get_location

class ApiClientTests(unittest.TestCase):
    
    def test_get_location_returns_expected_data(self):
        data_expected = {'country': 'United States', 'region': 'California',
                         'capital': 'Washington D.C.', 'cityName': 'Mountain View'}
        data_actual = get_location(ip='8.8.8.8')
        self.assertEqual(data_actual, data_expected)
