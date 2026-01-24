import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_all_zeros(self):
        self.assertEqual(re_order([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_all_non_zeros(self):
        self.assertEqual(re_order([1, 2, 3]), [1, 2, 3, 0])

    def test_mixed_values(self):
        self.assertEqual(re_order([1, 0, 2, 3, 0, 4]), [1, 2, 3, 4, 0, 0])

    def test_single_zero(self):
        self.assertEqual(re_order([0]), [0])

    def test_single_non_zero(self):
        self.assertEqual(re_order([1]), [1, 0])

    def test_large_list(self):
        self.assertEqual(re_order([1]*1000 + [0]*1000), [1]*1000 + [0]*1000)
