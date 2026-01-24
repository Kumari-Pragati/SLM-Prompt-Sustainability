import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(area_trapezium(0, 0, 10), 0)
        self.assertAlmostEqual(area_trapezium(100, 100, 0), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_trapezium(1, 1, 1), 0.5)
        self.assertAlmostEqual(area_trapezium(1000000, 1000000, 1), 5000000000.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_trapezium("5", 10, 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, "10", 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, 10, "7")
        with self.assertRaises(ValueError):
            area_trapezium(-1, 10, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, -1, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, 10, -1)
