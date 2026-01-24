import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(sort_sublists([['a', 'b'], ['c', 'd'], ['e', 'f']]), [['a', 'b'], ['c', 'd'], ['e', 'f']])

    def test_list_with_single_sublist(self):
        self.assertEqual(sort_sublists([['a']]), [['a']])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_list_with_empty_sublists(self):
        self.assertEqual(sort_sublists([[''], ['a']]), [[''], ['a']])

    def test_list_with_sublists_of_same_length(self):
        self.assertEqual(sort_sublists([['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]), [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']])

    def test_list_with_sublists_of_different_lengths(self):
        self.assertEqual(sort_sublists([['a', 'b'], ['c'], ['d', 'e', 'f']]), [['a', 'b'], ['c'], ['d', 'e', 'f']])

    def test_list_with_sublists_of_different_lengths_and_sorted(self):
        self.assertEqual(sort_sublists([['d', 'e', 'f'], ['c'], ['a', 'b']]), [['a', 'b'], ['c'], ['d', 'e', 'f']])

    def test_list_with_sublists_of_different_lengths_and_sorted_by_length(self):
        self.assertEqual(sort_sublists([['f', 'e', 'd'], ['c'], ['a', 'b']]), [['c'], ['a', 'b'], ['f', 'e', 'd']])
