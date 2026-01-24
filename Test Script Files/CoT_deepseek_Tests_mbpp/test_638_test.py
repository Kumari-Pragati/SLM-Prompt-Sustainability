import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(wind_chill(5, 10), 10)
        self.assertEqual(wind_chill(10, 0), 13)
        self.assertEqual(wind_chill(8, -5), 14)

    def test_edge_cases(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(15, 10), 10)
        self.assertEqual(wind_chill(20, -10), 13)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            wind_chill("5", 10)
        with self.assertRaises(TypeError):
            wind_chill(5, "10")
        with self.assertRaises(TypeError):
            wind_chill("5", "10")
        with self.assertRaises(ValueError):
            wind_chill(-5, 10)
        with self.assertRaises(ValueError):
            wind_chill(5, -10)
