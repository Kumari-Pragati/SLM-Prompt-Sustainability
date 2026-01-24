import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_single_list(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3]]), [[3, 2, 1]])

    def test_multiple_lists(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[3, 2, 1], [6, 5, 4], [9, 8, 7]])

    def test_duplicate_elements(self):
        self.assertEqual(reverse_list_lists([[1, 2, 2], [3, 3, 3]]), [[2, 2, 1], [3, 3, 3]])

    def test_single_element_lists(self):
        self.assertEqual(reverse_list_lists([[1], [2], [3]]), [[1], [2], [3]])

    def test_reverse_order(self):
        self.assertEqual(reverse_list_lists([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
