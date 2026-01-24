import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(median_trapezium(5, 5, 10), 5)

    def test_edge_case(self):
        self.assertEqual(median_trapezium(0, 10, 10), 5)

    def test_edge_case2(self):
        self.assertEqual(median_trapezium(10, 0, 10), 5)

    def test_edge_case3(self):
        self.assertEqual(median_trapezium(10, 10, 10), 10)

    def test_edge_case4(self):
        self.assertEqual(median_trapezium(0, 0, 10), 0)

    def test_edge_case5(self):
        self.assertEqual(median_trapezium(10, 10, 0), 0)

    def test_edge_case6(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0)
