import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(listify_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(listify_list([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_list_of_lists_with_empty_sublist(self):
        self.assertEqual(listify_list([[1, 2], [], [3, 4]]), [[1, 2], [], [3, 4]])

    def test_list_of_lists_with_sublist_of_length_one(self):
        self.assertEqual(listify_list([[1], [2, 3], [4]]), [[1], [2, 3], [4]])

    def test_list_of_lists_with_sublist_of_length_zero(self):
        self.assertEqual(listify_list([[1, 2], [3], []]), [[1, 2], [3], []])

    def test_list_of_lists_with_sublist_of_length_greater_than_one(self):
        self.assertEqual(listify_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
