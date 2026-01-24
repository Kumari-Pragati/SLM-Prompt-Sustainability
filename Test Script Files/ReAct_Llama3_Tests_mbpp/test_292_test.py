import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find(10, 2), 5)

    def test_edge_case_divisible_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_edge_case_divisible_by_nonzero(self):
        self.assertEqual(find(10, 1), 10)

    def test_edge_case_zero_dividend(self):
        self.assertEqual(find(0, 2), 0)

    def test_edge_case_zero_divisor(self):
        self.assertEqual(find(10, 0), 0)

    def test_edge_case_negative_dividend(self):
        self.assertEqual(find(-10, 2), -5)

    def test_edge_case_negative_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            find(-10, 0)

    def test_edge_case_large_dividend(self):
        self.assertEqual(find(1000, 2), 500)

    def test_edge_case_large_divisor(self):
        self.assertEqual(find(1000, 100), 10)
