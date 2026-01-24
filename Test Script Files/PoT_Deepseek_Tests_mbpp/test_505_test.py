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

    def test_mixed_elements(self):
        self.assertEqual(re_order([1, 0, 1, 0]), [1, 1, 0, 0])

    def test_single_element(self):
        self.assertEqual(re_order([0]), [0])
        self.assertEqual(re_order([1]), [1])

    def test_large_list(self):
        self.assertEqual(re_order([1]*1000 + [0]*1000), [1]*1000 + [0]*1000)

    def test_negative_numbers(self):
        self.assertEqual(re_order([-1, 0, -2, 0]), [-1, -2, 0, 0])

    def test_mixed_positive_negative(self):
        self.assertEqual(re_order([1, -1, 0, -1, 0]), [1, -1, -1, 0, 0])
