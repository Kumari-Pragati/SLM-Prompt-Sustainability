import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(wind_chill(20, -10), -25)

    def test_zero_wind_speed(self):
        self.assertEqual(wind_chill(0, -10), 13)

    def test_zero_temperature(self):
        self.assertEqual(wind_chill(20, 0), 13)

    def test_high_wind_speed(self):
        self.assertEqual(wind_chill(50, -10), -37)

    def test_high_temperature(self):
        self.assertEqual(wind_chill(20, 20), 13)

    def test_invalid_wind_speed(self):
        with self.assertRaises(TypeError):
            wind_chill('twenty', -10)

    def test_invalid_temperature(self):
        with self.assertRaises(TypeError):
            wind_chill(20,'minus ten')
