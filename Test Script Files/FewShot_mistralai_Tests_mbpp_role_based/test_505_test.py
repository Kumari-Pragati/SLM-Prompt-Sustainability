import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(re_order([3, None, 0, 2, 5, '', 4]), [3, 1, 0, 2, 5, '', 4])

    def test_negative_numbers(self):
        self.assertEqual(re_order([0, -1, 2, -3, 4]), [0, 1, 2, 0, 4])

    def test_all_none_and_empty_strings(self):
        self.assertEqual(re_order([None, None, None, '', None]), [None, None, None, None])

    def test_all_zero(self):
        self.assertEqual(re_order([0, 0, 0]), [0, 0, 0])
