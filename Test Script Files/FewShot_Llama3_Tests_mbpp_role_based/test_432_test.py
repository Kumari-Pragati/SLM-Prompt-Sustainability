import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(median_trapezium(3, 4, 5), 3.5)

    def test_zero_base(self):
        self.assertAlmostEqual(median_trapezium(0, 0, 5), 0)

    def test_negative_bases(self):
        self.assertAlmostEqual(median_trapezium(-3, -4, 5), -3.5)

    def test_zero_height(self):
        self.assertAlmostEqual(median_trapezium(3, 4, 0), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            median_trapezium('a', 'b', 5)
