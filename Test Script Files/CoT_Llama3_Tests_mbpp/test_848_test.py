import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):
    def test_area_trapezium_typical(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 3), 12.5)

    def test_area_trapezium_edge(self):
        self.assertAlmostEqual(area_trapezium(0, 0, 3), 0)

    def test_area_trapezium_zero_height(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 0), 0)

    def test_area_trapezium_negative_base(self):
        with self.assertRaises(TypeError):
            area_trapezium(-5, 5, 3)

    def test_area_trapezium_negative_height(self):
        with self.assertRaises(TypeError):
            area_trapezium(5, 5, -3)

    def test_area_trapezium_non_numeric_input(self):
        with self.assertRaises(TypeError):
            area_trapezium('five', 5, 3)
