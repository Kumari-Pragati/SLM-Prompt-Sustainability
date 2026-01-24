import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_area_trapezium_positive(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 5), 12.5)

    def test_area_trapezium_negative(self):
        with self.assertRaises(TypeError):
            area_trapezium(-5, 5, 5)

    def test_area_trapezium_zero(self):
        self.assertAlmostEqual(area_trapezium(0, 0, 5), 0)

    def test_area_trapezium_non_numeric(self):
        with self.assertRaises(TypeError):
            area_trapezium('five', 5, 5)

    def test_area_trapezium_non_numeric2(self):
        with self.assertRaises(TypeError):
            area_trapezium(5, 'five', 5)

    def test_area_trapezium_non_numeric3(self):
        with self.assertRaises(TypeError):
            area_trapezium('five', 'five', 5)
