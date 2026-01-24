import unittest
from mbpp_638_code import pow
from638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_wind_chill_valid_input(self):
        self.assertEqual(wind_chill(5, 288), 233)
        self.assertEqual(wind_chill(10, 288), 159)
        self.assertEqual(wind_chill(20, 288), 106)
        self.assertEqual(wind_chill(30, 288), 74)
        self.assertEqual(wind_chill(40, 288), 39)
        self.assertEqual(wind_chill(50, 288), 0)
        self.assertEqual(wind_chill(60, 288), 0)

    def test_wind_chill_invalid_input(self):
        self.assertRaises(ValueError, wind_chill, -1, 288)
        self.assertRaises(ValueError, wind_chill, 121, 288)
        self.assertRaises(ValueError, wind_chill, 5, -100)
        self.assertRaises(ValueError, wind_chill, 5, 300)
