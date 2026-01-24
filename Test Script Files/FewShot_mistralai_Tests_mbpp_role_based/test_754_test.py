import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_same_elements_in_lists(self):
        self.assertEqual(extract_index_list([1, 2, 3, 1], [2, 1, 3, 2], [1, 1, 1, 2]), [1])
        self.assertEqual(extract_index_list([4, 4, 4, 4], [4, 4, 4, 4], [4, 4, 4, 4]), [0, 1, 2, 3])

    def test_different_elements_in_lists(self):
        self.assertEqual(extract_index_list([1, 2, 3], [2, 1, 3], [1, 1, 1]), [])
        self.assertEqual(extract_index_list([1, 2, 3], [2, 1, 4], [1, 1, 1]), [])

    def test_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])
        self.assertEqual(extract_index_list([1], [], [1]), [])
        self.assertEqual(extract_index_list([], [1], [1]), [])

    def test_single_element_lists(self):
        self.assertEqual(extract_index_list([1], [1], [1]), [0])
        self.assertEqual(extract_index_list([1], [2], [1]), [])
        self.assertEqual(extract_index_list([1], [1], [2]), [])
