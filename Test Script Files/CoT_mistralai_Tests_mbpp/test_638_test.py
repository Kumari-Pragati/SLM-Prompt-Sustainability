import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_wind_chill_positive_temperature(self):
        self.assertEqual(wind_chill(3.0, 20), 17)
        self.assertEqual(wind_chill(5.0, 10), 15)
        self.assertEqual(wind_chill(10.0, 0), 23)

    def test_wind_chill_zero_temperature(self):
        self.assertEqual(wind_chill(3.0, 0), 213)
        self.assertEqual(wind_chill(5.0, 0), 175)
        self.assertEqual(wind_chill(10.0, 0), 91)

    def test_wind_chill_negative_temperature(self):
        self.assertEqual(wind_chill(3.0, -10), 63)
        self.assertEqual(wind_chill(5.0, -20), 57)
        self.assertEqual(wind_chill(10.0, -30), 47)

    def test_wind_chill_zero_wind_speed(self):
        self.assertEqual(wind_chill(0.0, 20), 17)
        self.assertEqual(wind_chill(0.0, -10), 63)

    def test_wind_chill_negative_wind_speed(self):
        self.assertEqual(wind_chill(-1.0, 20), 17)
        self.assertEqual(wind_chill(-1.0, -10), 63)

    def test_wind_chill_invalid_input(self):
        self.assertRaises(ValueError, wind_chill, -5.0, 20)
        self.assertRaises(ValueError, wind_chill, 3.0, -50)
