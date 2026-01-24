import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_equal_elements(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_different_elements(self):
        self.assertEqual(extract_index_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [])

    def test_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_unequal_lengths(self):
        self.assertEqual(extract_index_list([1, 2, 3, 4], [1, 2, 3], [1, 2, 3]), [1, 2, 3])
