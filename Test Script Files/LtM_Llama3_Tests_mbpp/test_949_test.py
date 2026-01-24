import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(sort_list([1]), '[1]')

    def test_multiple_elements_list(self):
        self.assertEqual(sort_list([1, 2, 3]), '[1, 2, 3]')

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list([1, 2, 2, 3, 3, 3]), '[1, 2, 2, 3, 3, 3]')

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_list([-1, 0, 1]), '[-1, 0, 1]')

    def test_list_with_zero(self):
        self.assertEqual(sort_list([0, 1]), '[0, 1]')

    def test_list_with_max_length(self):
        self.assertEqual(sort_list([1]*1000), '[1, 1, 1,..., 1]')

    def test_list_with_min_length(self):
        self.assertEqual(sort_list([1]), '[1]')
