import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])
        self.assertListEqual(re_order([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])
        self.assertListEqual(re_order([0, 0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0, 0])

    def test_edge_case_empty_list(self):
        self.assertListEqual(re_order([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(re_order([1]), [1, 0])

    def test_edge_case_all_zero(self):
        self.assertListEqual(re_order([0] * 10), [0] * 10)

    def test_corner_case_negative_numbers(self):
        self.assertListEqual(re_order([-1, 0, 2, 0, 3]), [-1, 2, 3, 0, 0])
