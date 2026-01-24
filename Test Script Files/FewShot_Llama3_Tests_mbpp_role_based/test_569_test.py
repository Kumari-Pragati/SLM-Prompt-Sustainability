import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([[1, 3, 2], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2, 2, 1], [3, 1, 1, 3]]), [[1, 1, 2, 2], [1, 1, 3, 3]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_sublists([[-1, 0, 1], [2, -3, 4]]), [[-3, -1, 0, 1], [2, 4]])
