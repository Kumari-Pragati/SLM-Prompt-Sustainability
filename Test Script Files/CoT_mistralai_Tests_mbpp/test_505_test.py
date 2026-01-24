import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(re_order([3, None, 2, 0, 5, None, 1]), [3, 1, 2, 0, 5])

    def test_all_none_list(self):
        self.assertEqual(re_order([None] * 10), [None] * 10)

    def test_all_zero_list(self):
        self.assertEqual(re_order([0] * 10), [0] * 10)

    def test_mixed_elements_list(self):
        self.assertEqual(re_order([None, 3, None, 0, 2, None, 1, None]), [3, 1, 2, 0])

    def test_negative_number(self):
        self.assertEqual(re_order([0, -1, 2]), [0, 2, 0])

    def test_float_number(self):
        self.assertEqual(re_order([0, 3.14, 2]), [3.14, 2, 0])

    def test_string_input(self):
        self.assertEqual(re_order(["a", None, "b", 0, "c", None, "d", None]), ["a", "d", "b", "c"])
