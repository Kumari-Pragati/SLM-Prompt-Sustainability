import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists_with_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_with_single_element_list(self):
        self.assertEqual(sort_sublists(['a']), ['a'])

    def test_sort_sublists_with_multiple_element_list(self):
        self.assertEqual(sort_sublists(['b', 'a', 'd', 'c']), ['a', 'b', 'c', 'd'])

    def test_sort_sublists_with_same_length_elements(self):
        self.assertEqual(sort_sublists(['abc', 'de', 'f']), ['f', 'de', 'abc'])

    def test_sort_sublists_with_different_length_elements(self):
        self.assertEqual(sort_sublists(['abc', 'de', 'fghi']), ['de', 'abc', 'fghi'])
