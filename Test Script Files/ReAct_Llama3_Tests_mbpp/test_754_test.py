import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_all_equal(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1])

    def test_no_equal(self):
        self.assertEqual(extract_index_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [])

    def test_some_equal(self):
        self.assertEqual(extract_index_list([1, 1, 2], [1, 2, 2], [1, 2, 3]), [1])

    def test_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_single_element_lists(self):
        self.assertEqual(extract_index_list([1], [1], [1]), [1])

    def test_long_list(self):
        self.assertEqual(extract_index_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
