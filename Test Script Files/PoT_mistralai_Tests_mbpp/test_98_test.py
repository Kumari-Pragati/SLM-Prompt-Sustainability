import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_num([1, 2, 3]), 1.5)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiply_num([]), 0)

    def test_edge_case_single_number(self):
        self.assertEqual(multiply_num([4]), 4 / 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(multiply_num([-1, -2, -3]), -0.75)

    def test_corner_case_zero(self):
        self.assertEqual(multiply_num([0, 1, 2]), 0)
