import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_empty_lists(self):
        """Test empty lists"""
        self.assertListEqual(extract_index_list([], [], []), [])
        self.assertListEqual(extract_index_list([1], [], [1]), [1])
        self.assertListEqual(extract_index_list([], [1], [1]), [])
        self.assertListEqual(extract_index_list([], [], []), [])

    def test_single_match(self):
        """Test single matching elements"""
        self.assertListEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1])
        self.assertListEqual(extract_index_list([1, 2, 3], [1, 2, 4], [1, 2, 3]), [])
        self.assertListEqual(extract_index_list([1, 2, 3], [1, 3, 4], [1, 2, 3]), [])

    def test_multiple_matches(self):
        """Test multiple matching elements"""
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 1, 3], [1, 2, 1, 3]), [1, 1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3, 1], [1, 2, 1, 3]), [1, 1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 3, 1, 2], [1, 2, 1, 3]), [1, 1])

    def test_mixed_matches(self):
        """Test mixed matches and non-matches"""
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3, 4], [1, 2, 1, 3]), [1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 3, 4, 2], [1, 2, 1, 3]), [1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [3, 4, 2, 1], [1, 2, 1, 3]), [])

    def test_lists_length(self):
        """Test lists with different lengths"""
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3], [1, 2, 1, 3]), [1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3, 4], [1, 2, 1, 3]), [1])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3], [1, 2, 1, 4]), [])
        self.assertListEqual(extract_index_list([1, 2, 1, 3], [1, 2, 3, 4], [1, 2, 1, 3, 5]), [])
