import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(zip_list([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(zip_list([1, 2, 3], []), [1, 2, 3])

    def test_edge_case_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5]), [5, 7])
        self.assertEqual(zip_list([1, 2], [3, 4, 5]), [4, 6])
        self.assertEqual(zip_list([1], [2, 3, 4]), [2, 3, 4])
        self.assertEqual(zip_list([1, 2], [3]), [3, 4])
        self.assertEqual(zip_list([1], [2, 3]), [2, 3])

    def test_edge_case_empty_lists(self):
        self.assertEqual(zip_list([], []), [])
