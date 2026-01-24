import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(wind_chill(15, 10), 25)
        self.assertEqual(wind_chill(10, 15), 25)
        self.assertEqual(wind_chill(20, 20), 25)

    def test_edge_cases(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(0, 30), 13)
        self.assertEqual(wind_chill(30, 0), 13)
        self.assertEqual(wind_chill(30, 30), 13)

    def test_boundary_conditions(self):
        self.assertEqual(wind_chill(-1, 10), 13)
        self.assertEqual(wind_chill(31, 10), 13)
        self.assertEqual(wind_chill(15, -1), 13)
        self.assertEqual(wind_chill(15, 31), 13)

    def test_special_cases(self):
        self.assertEqual(wind_chill(15, 0), 13)
        self.assertEqual(wind_chill(0, 15), 13)
        self.assertEqual(wind_chill(15, 30), 25)
        self.assertEqual(wind_chill(30, 15), 25)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            wind_chill('a', 10)
        with self.assertRaises(TypeError):
            wind_chill(15, 'a')
