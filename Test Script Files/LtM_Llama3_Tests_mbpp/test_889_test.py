import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_single_list(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3]]), [[3, 2, 1]])

    def test_multiple_lists(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_list_with_duplicates(self):
        self.assertEqual(reverse_list_lists([[1, 2, 2, 3, 3, 3]]), [[3, 3, 3, 2, 2, 1]])

    def test_list_with_negative_numbers(self):
        self.assertEqual(reverse_list_lists([[-1, -2, -3]]), [[-3, -2, -1]])

    def test_list_with_mixed_types(self):
        self.assertEqual(reverse_list_lists([[1, 'a', 2.5]]), [[2.5, 'a', 1]])

    def test_list_with_empty_sublist(self):
        self.assertEqual(reverse_list_lists([[1, 2, []], [3, 4, 5]]), [[[], 2, 1], [5, 4, 3]])

    def test_list_with_sublist_of_lists(self):
        self.assertEqual(reverse_list_lists([[1, [2, 3], 4], [5, 6, 7]]), [[7, [3, 2], 4], [6, 5, 1]])
