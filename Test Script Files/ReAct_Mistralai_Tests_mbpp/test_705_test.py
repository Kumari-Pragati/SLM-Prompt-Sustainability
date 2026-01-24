import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(sort_sublists([1]), [1])

    def test_sort_two_element_list(self):
        self.assertEqual(sort_sublists([3, 1]), [1, 3])

    def test_sort_multiple_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_sort_mixed_types(self):
        self.assertEqual(sort_sublists([[1, 'a'], [2, 'b'], [3, 'c']]),
                         [[[1, 'a']], [ [2, 'b'] ], [ [3, 'c'] ]])

    def test_sort_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2], [1, 3], [2, 2]]),
                         [[[1, 2], [1, 3]], [ [2, 2] ]])

    def test_sort_sublists_with_longer_sublists_first(self):
        self.assertEqual(sort_sublists([[3, 2], [1, 2], [3, 1]]),
                         [[[3, 2]], [ [1, 2] ], [ [3, 1] ]])

    def test_sort_sublists_with_shorter_sublists_first(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 2], [3, 1]]),
                         [[[1, 2]], [ [3, 2] ], [ [3, 1] ]])

    def test_sort_sublists_with_equal_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 2], [3, 1]]),
                         [[[1, 2], [3, 2]], [ [3, 1] ]])

    def test_sort_sublists_with_negative_numbers(self):
        self.assertEqual(sort_sublists([[-3, 2], [-1, 2], [1, 2]]),
                         [[[-3, 2], [-1, 2]], [ [1, 2] ]])

    def test_sort_sublists_with_strings(self):
        self.assertEqual(sort_sublists(['abc', 'def', 'ghi']), ['abc', 'def', 'ghi'])

    def test_sort_sublists_with_mixed_types(self):
        self.assertEqual(sort_sublists([[1, 'a'], [2, 'b'], [3, 'c']]),
                         [[[1, 'a']], [ [2, 'b'] ], [ [3, 'c'] ]])

    def test_sort_sublists_with_empty_sublists(self):
        self.assertEqual(sort_sublists([[], [1], [2, 3]]), [[], [1], [2, 3]])
