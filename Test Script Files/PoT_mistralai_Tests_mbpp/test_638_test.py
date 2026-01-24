import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(wind_chill(30, 20), 13)
        self.assertEqual(wind_chill(40, 10), 15)
        self.assertEqual(wind_chill(50, 0), 35)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(wind_chill(0, 30), 0)
        self.assertEqual(wind_chill(100, -10), 86)
        self.assertEqual(wind_chill(-10, -10), -273)
        self.assertEqual(wind_chill(100, 100), 0)
