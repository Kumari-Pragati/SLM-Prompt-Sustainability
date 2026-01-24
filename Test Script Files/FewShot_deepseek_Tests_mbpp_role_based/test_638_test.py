import unittest
from mbpp_638_code import wind_chill

class TestWindChill(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(wind_chill(5, 10), 10)

    def test_boundary_conditions(self):
        self.assertEqual(wind_chill(0, 0), 13)
        self.assertEqual(wind_chill(10, 20), 10)
        self.assertEqual(wind_chill(10, -20), -10)

    def test_edge_conditions(self):
        self.assertEqual(wind_chill(12, 30), 0)
        self.assertEqual(wind_chill(15, 40), -10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            wind_chill("5", 10)
        with self.assertRaises(TypeError):
            wind_chill(5, "10")
        with self.assertRaises(TypeError):
            wind_chill("5", "10")
