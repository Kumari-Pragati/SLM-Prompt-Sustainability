import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_empty_list(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_single_list(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3]]), [[3, 2, 1]])

    def test_single_element_list(self):
        self.assertEqual(reverse_list_lists([[1]]), [[1]])

    def test_empty_list_of_lists(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_list_of_empty_lists(self):
        self.assertEqual(reverse_list_lists([[], [], []]), [[], [], []])

    def test_list_of_single_element_lists(self):
        self.assertEqual(reverse_list_lists([[1], [2], [3]]), [[3], [2], [1]])
