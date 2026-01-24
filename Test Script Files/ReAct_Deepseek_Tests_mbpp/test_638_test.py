import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(wind_chill(5, 10), 10)
        self.assertEqual(wind_chill(10, 0), 13)
        self.assertEqual(wind_chill(8, -5), 16)

    def test_boundary_cases(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(15, 10), 10)
        self.assertEqual(wind_chill(20, -10), 13)

    def test_negative_values(self):
        self.assertEqual(wind_chill(-5, 10), 10)
        self.assertEqual(wind_chill(5, -10), 13)

    def test_high_values(self):
        self.assertEqual(wind_chill(30, 10), 0)
        self.assertEqual(wind_chill(30, -10), 13)

    def test_high_speed_values(self):
        self.assertEqual(wind_chill(50, 10), 0)
        self.assertEqual(wind_chill(50, -10), 13)

    def test_low_speed_values(self):
        self.assertEqual(wind_chill(3, 10), 13)
        self.assertEqual(wind_chill(3, -10), 13)
