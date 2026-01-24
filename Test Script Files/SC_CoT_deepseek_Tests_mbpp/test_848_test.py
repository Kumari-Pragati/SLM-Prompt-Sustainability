import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_trapezium(0, 0, 10), 0)
        self.assertAlmostEqual(area_trapezium(5, 10, 0), 0)
        self.assertAlmostEqual(area_trapezium(0, 10, 7), 0)
        self.assertAlmostEqual(area_trapezium(5, 0, 7), 0)

    def test_special_cases(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 7), 35)
        self.assertAlmostEqual(area_trapezium(10, 10, 7), 70)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_trapezium("5", 10, 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, "10", 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, 10, "7")
        with self.assertRaises(ValueError):
            area_trapezium(-5, 10, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, -10, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, 10, -7)
