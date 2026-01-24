import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[5, 3, 2], [9, 1, 7]]), [[2, 3, 5], [1, 7, 9]])

    def test_empty_sublist(self):
        self.assertEqual(sort_sublists([[], [9, 1, 7]]), [ [], [1, 7, 9]])

    def test_single_element_sublist(self):
        self.assertEqual(sort_sublists([[5], [9, 1, 7]]), [[5], [1, 7, 9]])

    def test_sorted_sublist(self):
        self.assertEqual(sort_sublists([[2, 3, 5], [1, 7, 9]]), [[2, 3, 5], [1, 7, 9]])

    def test_negative_numbers(self):
        self.assertEqual(sort_sublists([[-5, -3, -2], [-9, -1, -7]]), [[-5, -3, -2], [-9, -7, -1]])

    def test_mixed_numbers(self):
        self.assertEqual(sort_sublists([[5, -3, 2], [9, -1, 7]]), [[-3, 2, 5], [-1, 7, 9]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])
