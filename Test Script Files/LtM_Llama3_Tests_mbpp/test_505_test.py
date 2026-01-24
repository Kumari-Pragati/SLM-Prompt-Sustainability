import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(re_order([]), [])

    def test_single_element_list(self):
        self.assertEqual(re_order([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(re_order([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_list_with_duplicates(self):
        self.assertEqual(re_order([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_list_with_zero(self):
        self.assertEqual(re_order([0, 1, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_list_with_negative_numbers(self):
        self.assertEqual(re_order([-1, -2, 0, 1, 2]), [-2, -1, 0, 1, 2])

    def test_list_with_mixed_types(self):
        self.assertEqual(re_order([1, 'a', 2, 'b', 3]), [1, 2, 3, 'a', 'b'])

    def test_list_with_empty_string(self):
        self.assertEqual(re_order(['a', '', 'b', 'c']), ['a', 'b', 'c', '', ''])
