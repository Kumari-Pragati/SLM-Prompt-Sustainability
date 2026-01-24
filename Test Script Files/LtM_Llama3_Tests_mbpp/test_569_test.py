import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([[1, 3, 2], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_empty_sublists(self):
        self.assertEqual(sort_sublists([[], [1, 2, 3]]), [[], [1, 2, 3]])

    def test_unsorted_sublists(self):
        self.assertEqual(sort_sublists([[3, 1, 2], [5, 4, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_sorted_sublists(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_mixed_types(self):
        self.assertEqual(sort_sublists([[1, 2, 3], ['a', 'b', 'c']]), [[1, 2, 3], ['a', 'b', 'c']])
