import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):
    def test_reverse_empty_list(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_reverse_single_list(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3]]), [[3, 2, 1]])

    def test_reverse_multiple_lists(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_reverse_list_with_duplicates(self):
        self.assertEqual(reverse_list_lists([[1, 1, 2, 3], [4, 4, 5, 6], [7, 7, 8, 9]]), [[9, 8, 7, 7], [6, 5, 4, 4], [3, 2, 1, 1]])

    def test_reverse_list_with_strings(self):
        self.assertEqual(reverse_list_lists([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), [['i', 'h', 'g'], ['f', 'e', 'd'], ['c', 'b', 'a']])
