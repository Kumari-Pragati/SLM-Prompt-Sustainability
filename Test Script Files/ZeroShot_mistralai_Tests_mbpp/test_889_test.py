import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_single_list(self):
        self.assertEqual(reverse_list_lists([[1]]), [[1]])
        self.assertEqual(reverse_list_lists([[3]]), [[3]])
        self.assertEqual(reverse_list_lists([[5]]), [[5]])

    def test_multiple_lists(self):
        self.assertEqual(reverse_list_lists([[1, 2], [3, 4], [5, 6]]), [[2, 1], [4, 3], [6, 5]])
        self.assertEqual(reverse_list_lists([[10, 9], [8, 7], [6, 5]]), [[9, 10], [7, 8], [5, 6]])
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3, 2, 1], [6, 5, 4], [9, 8, 7]])
