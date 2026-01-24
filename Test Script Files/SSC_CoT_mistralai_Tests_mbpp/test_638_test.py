import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(wind_chill(30, 5), 23)
        self.assertEqual(wind_chill(40, 10), 18)
        self.assertEqual(wind_chill(50, 20), 10)

    def test_edge_cases(self):
        self.assertEqual(wind_chill(0, -20), 0)
        self.assertEqual(wind_chill(150, 10), 10)
        self.assertEqual(wind_chill(0, 0), 1312)

    def test_boundary_conditions(self):
        self.assertEqual(wind_chill(29, 5), 23)
        self.assertEqual(wind_chill(31, 5), 23)
        self.assertEqual(wind_chill(41, 10), 18)
        self.assertEqual(wind_chill(51, 20), 10)
