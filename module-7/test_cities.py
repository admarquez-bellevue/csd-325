import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        """Test if city_country returns correctly formatted string"""
        result = city_country("omaha", "united states")
        self.assertEqual(result, "Omaha, United States")

if __name__ == "__main__":
    unittest.main()