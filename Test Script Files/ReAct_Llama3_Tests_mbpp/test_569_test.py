import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_sublists_of_differing_lengths(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6, 7, 8, 9]]), [[1, 2, 3], [4, 5], [6, 7, 8, 9]])

    def test_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2, 2, 3], [4, 4, 5, 5, 6]]), [[1, 2, 2, 3], [4, 4, 5, 5, 6]])

    def test_sublists_with_negative_numbers(self):
        self.assertEqual(sort_sublists([[-1, 0, 1], [2, -3, 4]]), [[-1, 0, 1], [2, -3, 4]])

    def test_sublists_with_mixed_types(self):
        self.assertEqual(sort_sublists([['a', 'b', 'c'], [1, 2, 3.14]]), [['a', 'b', 'c'], [1, 2, 3.14]])
