import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(re_order([3, None, 1, 2, None, 5, None]), [3, 1, 2, 5])

    def test_all_none_list(self):
        self.assertEqual(re_order([None] * 10), [None] * 10)

    def test_all_zero_list(self):
        self.assertEqual(re_order([0] * 10), [0] * 10)

    def test_list_with_zero(self):
        self.assertEqual(re_order([0, 1, 2, None, 0, 4, 5]), [0, 1, 2, 4, 5])
