import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_zero_base(self):
        with self.assertRaises(ValueError):
            area_trapezium(0, base2=1, height=2)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            area_trapezium(-1, base2=-2, height=3)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            area_trapezium(1, base2=2, height=0)

    def test_positive_values(self):
        self.assertAlmostEqual(area_trapezium(3, 4, 5), 30.0)
        self.assertAlmostEqual(area_trapezium(1, 2, 3), 6.0)
        self.assertAlmostEqual(area_trapezium(0.5, 1.5, 2), 2.25)
