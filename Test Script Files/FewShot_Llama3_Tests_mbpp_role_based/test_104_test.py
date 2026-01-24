import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_sublists([[3, 1, 2], [2, 3, 1], [1, 2, 3]]), [[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_sublists([[3, 1, 2, 2], [2, 3, 1, 1], [1, 2, 3, 3]]), [[1, 1, 2, 2, 3, 3], [1, 2, 3], [1, 2, 3]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_sublists([[-3, -1, -2], [-2, -3, -1], [-1, -2, -3]]), [[-3, -1, -2], [-2, -3, -1], [-1, -2, -3]])
