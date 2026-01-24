import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(wind_chill(5, 10), 10)
        self.assertEqual(wind_chill(10, 20), 17)

    def test_edge_conditions(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(5, 0), 13)
        self.assertEqual(wind_chill(0, 10), 13)
        self.assertEqual(wind_chill(10, 10), 13)

    def test_complex_cases(self):
        self.assertEqual(wind_chill(15, 20), 10)
        self.assertEqual(wind_chill(20, 30), 5)
