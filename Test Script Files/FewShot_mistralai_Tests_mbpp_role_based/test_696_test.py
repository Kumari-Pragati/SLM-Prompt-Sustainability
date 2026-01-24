import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):
    def test_zip_equal_length_lists(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_zip_lists_with_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [(1, 4), (2, 5)])

    def test_empty_list(self):
        self.assertEqual(zip_list([], [1, 2, 3]), [])

    def test_list_with_none(self):
        self.assertEqual(zip_list([None], [1, 2, 3]), [None, 1, 2, 3])
