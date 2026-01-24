import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(zip_list([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[1, 2, 5, 6], [3, 4, 7, 8]])

    def test_empty_list(self):
        self.assertEqual(zip_list([], []), [])

    def test_single_element_list(self):
        self.assertEqual(zip_list([[1]], [[2]]), [[1, 2]])

    def test_list_of_lists(self):
        self.assertEqual(zip_list([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]), [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]])

    def test_list_of_lists_with_differing_lengths(self):
        self.assertEqual(zip_list([[1, 2, 3], [4, 5]], [[7, 8, 9, 10, 11, 12]]), [[1, 2, 3, 7, 8, 9], [4, 5, 10, 11, 12]])

    def test_list_of_lists_with_differing_lengths_and_empty(self):
        self.assertEqual(zip_list([[1, 2, 3], [], [4, 5, 6]], [[7, 8, 9, 10, 11, 12]]), [[1, 2, 3, 7, 8, 9], [4, 5, 6, 10, 11, 12]])
