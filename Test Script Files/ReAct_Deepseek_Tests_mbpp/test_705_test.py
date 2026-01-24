import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_same_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_different_length_sublists(self):
        self.assertEqual(sort_sublists([[1], [2, 3], [4, 5, 6]]), [[1], [2, 3], [4, 5, 6]])

    def test_sorted_sublists(self):
        self.assertEqual(sort_sublists([[2, 1], [4, 3]]), [[1, 2], [3, 4]])

    def test_empty_sublists(self):
        self.assertEqual(sort_sublists([[], []]), [])

    def test_single_element_sublists(self):
        self.assertEqual(sort_sublists([[1], [2], [3]]), [[1], [2], [3]])

    def test_negative_numbers(self):
        self.assertEqual(sort_sublists([[-1, -2], [-3, -4]]), [[-2, -1], [-4, -3]])

    def test_mixed_numbers(self):
        self.assertEqual(sort_sublists([[1, -1], [2, -2]]), [[-2, 2], [-1, 1]])
