import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(re_order([1, 1, 0, 2, 2, 0, 3, 3]), [1, 2, 3])

    def test_list_with_zeros(self):
        self.assertEqual(re_order([0, 1, 0, 2, 0, 3]), [1, 2, 3])

    def test_list_with_zeros_at_end(self):
        self.assertEqual(re_order([1, 2, 3, 0, 0]), [1, 2, 3])

    def test_list_with_zeros_and_non_zeros(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4])
