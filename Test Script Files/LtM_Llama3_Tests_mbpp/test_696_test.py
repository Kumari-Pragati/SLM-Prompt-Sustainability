import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(zip_list([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(zip_list([1], [2]), [[1, 2]])

    def test_lists_of_equal_length(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])

    def test_lists_of_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [[1, 4], [2, 5], [3]])

    def test_lists_of_zero_length(self):
        self.assertEqual(zip_list([], []), [])

    def test_lists_of_zero_length_with_nonzero(self):
        self.assertEqual(zip_list([1, 2, 3], []), [[1, 2, 3]])

    def test_lists_of_nonzero_length_with_zero(self):
        self.assertEqual(zip_list([], [4, 5, 6]), [[4, 5, 6]])
