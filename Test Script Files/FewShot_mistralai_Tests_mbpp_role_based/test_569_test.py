import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_sort_sublists_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_sort_sublists_simple_list(self):
        self.assertEqual(sort_sublists([[3, 1], [2, 4], [5, 6]]), [[1, 3], [2, 4], [5, 6]])

    def test_sort_sublists_mixed_lists(self):
        self.assertEqual(sort_sublists([[3, 1], [2, 4], [5, 6], [1, 3]]), [[1, 1, 3, 3], [2, 4], [5, 6]])

    def test_sort_sublists_negative_numbers(self):
        self.assertEqual(sort_sublists([[-3, -1], [-2, -4], [-5, -6]]), [[-6, -5], [-4, -2], [-1, -3]])
