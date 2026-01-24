import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_multiple_sublists(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_sublists_of_differing_lengths(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6, 7, 8, 9]]), [[1, 2, 3], [4, 5], [6, 7, 8, 9]])

    def test_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2, 2, 1], [3, 4, 5, 5, 3], [6, 7, 8, 9, 9]]), [[1, 1, 2, 2], [3, 3, 4, 5, 5], [6, 7, 8, 9, 9]])

    def test_sublists_with_negative_numbers(self):
        self.assertEqual(sort_sublists([[-1, 0, 1], [2, -3, 4], [5, 6, -7]]), [[-1, 0, 1], [-3, 2, 4], [-7, 5, 6]])
