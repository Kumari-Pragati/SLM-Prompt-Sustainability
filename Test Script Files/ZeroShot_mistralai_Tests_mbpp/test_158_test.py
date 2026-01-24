import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_min_ops_valid_input(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 4), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 5), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 6), -1)

    def test_min_ops_empty_list(self):
        self.assertEqual(min_Ops([], 0, 1), 0)

    def test_min_ops_single_element(self):
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertEqual(min_Ops([1], 1, 2), -1)

    def test_min_ops_negative_numbers(self):
        self.assertEqual(min_Ops([-1, -2, -3, -4, -5], 5, 2), 10)

    def test_min_ops_k_greater_than_n(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 6), -1)

    def test_min_ops_k_less_than_1(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 0), -1)
