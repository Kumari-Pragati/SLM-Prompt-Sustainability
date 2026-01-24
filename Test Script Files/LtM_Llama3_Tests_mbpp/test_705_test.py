import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([1, 2, 3]), [1, 2, 3])

    def test_empty_list_with_duplicates(self):
        self.assertEqual(sort_sublists([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_sublists([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_list_with_duplicates_sorted_by_length(self):
        self.assertEqual(sort_sublists(['abc', 'ab', 'a']), ['a', 'ab', 'abc'])

    def test_list_with_duplicates_sorted_by_length_empty(self):
        self.assertEqual(sort_sublists(['', 'a', 'abc']), ['', 'a', 'abc'])

    def test_list_with_duplicates_sorted_by_length_empty_duplicates(self):
        self.assertEqual(sort_sublists(['', '', 'a', 'abc']), ['', '', 'a', 'abc'])
