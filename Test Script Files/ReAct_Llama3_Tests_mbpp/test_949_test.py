import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(sort_list(['a']), '["a"]')

    def test_multiple_elements_list(self):
        self.assertEqual(sort_list(['a', 'b', 'c']), '["a", "b", "c"]')

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list(['a', 'b', 'a', 'c']), '["a", "a", "b", "c"]')

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_list([-1, 0, 1]), '["0", "-1", "1"]')

    def test_list_with_zero(self):
        self.assertEqual(sort_list([0, 1]), '["0", "1"]')

    def test_list_with_negative_and_positive_numbers(self):
        self.assertEqual(sort_list([-1, 0, 1, 2]), '["-1", "0", "1", "2"]')

    def test_list_with_empty_string(self):
        self.assertEqual(sort_list(['', 'a', 'b']), '["", "a", "b"]')

    def test_list_with_empty_string_and_numbers(self):
        self.assertEqual(sort_list(['', 0, 1]), '["", "0", "1"]')
