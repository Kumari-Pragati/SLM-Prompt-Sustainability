import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(5, 0), 13)
        self.assertEqual(wind_chill(10, 0), 13)
        self.assertEqual(wind_chill(0, 10), 13)
        self.assertEqual(wind_chill(5, 10), 13)
        self.assertEqual(wind_chill(10, 10), 13)

    def test_edge_cases(self):
        self.assertEqual(wind_chill(0, -10), 13)
        self.assertEqual(wind_chill(0, 20), 13)
        self.assertEqual(wind_chill(5, -10), 13)
        self.assertEqual(wind_chill(5, 20), 13)
        self.assertEqual(wind_chill(10, -10), 13)
        self.assertEqual(wind_chill(10, 20), 13)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            wind_chill('a', 0)
        with self.assertRaises(TypeError):
            wind_chill(0, 'a')
        with self.assertRaises(TypeError):
            wind_chill(None, 0)
        with self.assertRaises(TypeError):
            wind_chill(0, None)
