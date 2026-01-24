import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3], [4, 5, 6]]), [[3, 2, 1], [6, 5, 4]])

    def test_empty_input(self):
        self.assertEqual(reverse_list_lists([]), [])

    def test_single_list_input(self):
        self.assertEqual(reverse_list_lists([[1, 2, 3]]), [[3, 2, 1]])

    def test_duplicate_elements(self):
        self.assertEqual(reverse_list_lists([[1, 2, 2], [3, 3, 3]]), [[2, 2, 1], [3, 3, 3]])

    def test_negative_numbers(self):
        self.assertEqual(reverse_list_lists([[-1, -2, -3], [-4, -5, -6]]), [[-3, -2, -1], [-6, -5, -4]])

    def test_mixed_numbers(self):
        self.assertEqual(reverse_list_lists([[1, -2, 3], [-4, 5, 6]]), [[3, -2, 1], [6, 5, -4]])
