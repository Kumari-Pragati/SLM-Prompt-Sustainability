import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_positive_temperature_and_wind_speed(self):
        self.assertEqual(wind_chill(10, 20), 15)
        self.assertEqual(wind_chill(30, 5), 10)

    def test_zero_temperature_and_wind_speed(self):
        self.assertEqual(wind_chill(0, 0), 0)

    def test_negative_temperature_and_wind_speed(self):
        self.assertEqual(wind_chill(-10, 10), -23)
        self.assertEqual(wind_chill(-20, 20), -30)

    def test_zero_wind_speed(self):
        self.assertEqual(wind_chill(10, 0), 10)

    def test_negative_wind_speed(self):
        self.assertEqual(wind_chill(10, -10), 10)
