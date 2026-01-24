import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_trapezium(2, 3, 1), 2.5)

    def test_edge_case_zero_base(self):
        self.assertEqual(median_trapezium(0, 3, 1), 1.5)

    def test_edge_case_negative_base(self):
        self.assertEqual(median_trapezium(-2, 3, 1), 1.5)

    def test_edge_case_zero_height(self):
        self.assertEqual(median_trapezium(2, 3, 0), 2.5)

    def test_edge_case_negative_height(self):
        self.assertEqual(median_trapezium(2, 3, -1), 2.5)
