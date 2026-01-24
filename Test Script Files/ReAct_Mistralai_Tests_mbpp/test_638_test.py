import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_wind_chill_positive_temperature(self):
        self.assertEqual(wind_chill(10, 20), 17)
        self.assertEqual(wind_chill(25, 10), 15)
        self.assertEqual(wind_chill(30, 0), 0)

    def test_wind_chill_zero_temperature(self):
        self.assertEqual(wind_chill(10, 0), 0)
        self.assertEqual(wind_chill(0, 0), 0)

    def test_wind_chill_negative_temperature(self):
        self.assertEqual(wind_chill(10, -10), -23)
        self.assertEqual(wind_chill(0, -20), -35)

    def test_wind_chill_zero_wind_speed(self):
        self.assertEqual(wind_chill(0, 20), 20)

    def test_wind_chill_negative_wind_speed(self):
        self.assertEqual(wind_chill(-10, 20), 17)

    def test_wind_chill_extreme_wind_speed(self):
        self.assertEqual(wind_chill(100, 20), 17)
