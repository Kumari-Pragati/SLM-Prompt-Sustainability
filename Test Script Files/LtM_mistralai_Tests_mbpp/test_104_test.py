import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(sort_sublists([[3, 'a'], [1, 'b'], [4, 'c'], [1, 'a']]),
                              [[[1, 'a'], [1, 'a']], [ [3, 'a'], [1, 'b'] ], [ [4, 'c'] ]])

    def test_empty_list(self):
        self.assertListEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertListEqual(sort_sublists([[1, 'a']]), [[[1, 'a']]])

    def test_negative_numbers(self):
        self.assertListEqual(sort_sublists([[-3, 'a'], [1, 'b'], [-4, 'c'], [1, 'a']]),
                              [[[-3, 'a'], [-4, 'c']], [ [1, 'b'] ], [ [1, 'a'] ]])

    def test_mixed_numbers_and_strings(self):
        self.assertListEqual(sort_sublists([[3, 'a'], [1, 'b'], [4, 'c'], [1, 2], [1, 'a']]),
                              [[[1, 2], [1, 'a']], [ [3, 'a'], [1, 'b'] ], [ [4, 'c'] ]])

    def test_duplicate_sublists(self):
        self.assertListEqual(sort_sublists([[3, 'a'], [1, 'b'], [4, 'c'], [1, 'a'], [1, 'a']]),
                              [[[1, 'a'], [1, 'a']], [ [3, 'a'], [1, 'b'] ], [ [4, 'c'] ]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_sublists(123)
