import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(zip_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(zip_list([1], [2]), [[1, 2]])

    def test_lists_of_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [[1, 4], [2, 5], [3, None]])

    def test_lists_of_equal_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])

    def test_lists_with_duplicates(self):
        self.assertEqual(zip_list([1, 2, 2, 3], [4, 5, 5, 6]), [[1, 4], [2, 5], [2, 5], [3, 6]])

    def test_lists_with_none(self):
        self.assertEqual(zip_list([1, 2, None], [4, 5, 6]), [[1, 4], [2, 5], [None, 6]])
