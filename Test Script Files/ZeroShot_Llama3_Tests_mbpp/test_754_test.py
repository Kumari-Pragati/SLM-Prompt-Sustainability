import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_extract_index_list(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1])
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 4], [1, 2, 3]), [1, 2])
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3, 4]), [1, 2])
        self.assertEqual(extract_index_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4])

    def test_extract_index_list_empty_list(self):
        self.assertEqual(extract_index_list([], [], []), [])
        self.assertEqual(extract_index_list([1], [], []), [])
        self.assertEqual(extract_index_list([], [1], []), [])
        self.assertEqual(extract_index_list([], [], [1]), [])
