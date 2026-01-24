import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_num([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_zero(self):
        self.assertEqual(multiply_num([0, 1, 2, 3, 4]), 2.0)

    def test_edge_case_one(self):
        self.assertEqual(multiply_num([1, 1, 1, 1, 1]), 1.0)

    def test_edge_case_empty(self):
        self.assertRaises(ZeroDivisionError, multiply_num, [])

    def test_edge_case_single(self):
        self.assertEqual(multiply_num([1]), 1.0)

    def test_edge_case_negative(self):
        self.assertEqual(multiply_num([-1, -2, -3, -4, -5]), -3.0)

    def test_edge_case_mixed(self):
        self.assertEqual(multiply_num([1, -2, 3, -4, 5]), 0.0)
