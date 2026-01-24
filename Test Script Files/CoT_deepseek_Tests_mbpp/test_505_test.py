import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_all_zeros(self):
        self.assertEqual(re_order([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_all_ones(self):
        self.assertEqual(re_order([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_mixed_ones_zeros(self):
        self.assertEqual(re_order([1, 0, 1, 0]), [1, 1, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(re_order([-1, 0, 2, 0, -3]), [-1, 2, -3, 0, 0])

    def test_large_numbers(self):
        self.assertEqual(re_order([100, 0, 200, 0, 300]), [100, 200, 300, 0, 0])

    def test_large_list(self):
        self.assertEqual(re_order(list(range(1, 101))), list(range(1, 101)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            re_order("1, 0, 2, 0, 3")

        with self.assertRaises(TypeError):
            re_order(123456)

        with self.assertRaises(TypeError):
            re_order(None)
