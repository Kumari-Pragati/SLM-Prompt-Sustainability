import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(wind_chill(15, 0), 13)
        self.assertEqual(wind_chill(20, 10), 2)
        self.assertEqual(wind_chill(5, 5), 10)

    def test_edge_cases(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(30, 20), -24)
        self.assertEqual(wind_chill(40, 30), -51)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            wind_chill('a', 10)
        with self.assertRaises(TypeError):
            wind_chill(15, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(wind_chill(-1, 0), 13)
        self.assertEqual(wind_chill(100, 20), -51)
        self.assertEqual(wind_chill(0, 30), 13)
