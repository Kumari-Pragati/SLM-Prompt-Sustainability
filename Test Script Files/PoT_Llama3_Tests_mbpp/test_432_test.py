import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_trapezium(5, 10, 3), 7.5)

    def test_edge_case_base1_zero(self):
        self.assertEqual(median_trapezium(0, 10, 3), 5)

    def test_edge_case_base2_zero(self):
        self.assertEqual(median_trapezium(5, 0, 3), 2.5)

    def test_edge_case_height_zero(self):
        with self.assertRaises(ZeroDivisionError):
            median_trapezium(5, 10, 0)

    def test_edge_case_base1_and_base2_zero(self):
        with self.assertRaises(ZeroDivisionError):
            median_trapezium(0, 0, 3)

    def test_edge_case_base1_and_base2_negative(self):
        with self.assertRaises(ValueError):
            median_trapezium(-5, -10, 3)

    def test_edge_case_height_negative(self):
        with self.assertRaises(ValueError):
            median_trapezium(5, 10, -3)
