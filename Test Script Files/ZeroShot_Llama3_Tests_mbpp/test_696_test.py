import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_zip_list(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(zip_list([1, 2], [3, 4, 5]), [[1, 3], [2, 4]])
        self.assertEqual(zip_list([1, 2, 3, 4], [5, 6]), [[1, 5], [2, 6], [3, 4]])
        self.assertEqual(zip_list([], [1, 2, 3]), [])
        self.assertEqual(zip_list([1, 2, 3], []), [])

    def test_zip_list_empty(self):
        self.assertEqual(zip_list([], []), [])
        self.assertEqual(zip_list([1, 2, 3], []), [])
        self.assertEqual(zip_list([], [1, 2, 3]), [])
