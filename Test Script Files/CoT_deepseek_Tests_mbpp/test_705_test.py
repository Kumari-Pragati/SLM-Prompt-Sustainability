import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6]]), [[6], [4, 5], [1, 2, 3]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_same_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_mixed_length_sublists(self):
        self.assertEqual(sort_sublists([[1], [2, 3], [4, 5, 6]]), [[1], [2, 3], [4, 5, 6]])

    def test_unsorted_sublists(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [5, 4], [6]]), [[6], [5, 4], [3, 2, 1]])

    def test_negative_numbers(self):
        self.assertEqual(sort_sublists([[-1, -2, -3], [-4, -5], [-6]]), [[-6], [-4, -5], [-3, -2, -1]])

    def test_mixed_numbers(self):
        self.assertEqual(sort_sublists([[1, -2, 3], [4, -5], [6]]), [[6], [4, -5], [1, -2, 3]])
