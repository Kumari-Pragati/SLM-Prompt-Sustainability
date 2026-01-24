import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(extract_index_list([], [], []), [])
        self.assertListEqual(extract_index_list([1], [], [1]), [1])
        self.assertListEqual(extract_index_list([], [1], [1]), [])
        self.assertListEqual(extract_index_list([], [], []), [])

    def test_single_match(self):
        self.assertListEqual(extract_index_list([1, 2, 3], [2, 2, 3], [1, 2, 2]), [2])
        self.assertListEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 2]), [])
        self.assertListEqual(extract_index_list([1, 2, 3], [1, 2, 4], [1, 2, 2]), [])

    def test_multiple_matches(self):
        self.assertListEqual(extract_index_list([1, 2, 2, 3], [2, 2, 3, 3], [1, 2, 2, 2]), [2])
        self.assertListEqual(extract_index_list([1, 2, 2, 3], [2, 2, 3, 4], [1, 2, 2, 2]), [])
        self.assertListEqual(extract_index_list([1, 2, 2, 3], [1, 2, 3, 3], [1, 2, 2, 2]), [])

    def test_no_matches(self):
        self.assertListEqual(extract_index_list([1, 2, 2, 3], [2, 3, 4, 5], [1, 2, 2, 2]), [])
