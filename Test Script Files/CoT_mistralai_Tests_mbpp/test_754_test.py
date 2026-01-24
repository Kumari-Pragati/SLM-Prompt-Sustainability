import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(extract_index_list([], [], []), [])
        self.assertListEqual(extract_index_list([1], [], [1]), [1])
        self.assertListEqual(extract_index_list([], [1], [1]), [])
        self.assertListEqual(extract_index_list([], [], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(extract_index_list([1], [1], [1]), [1])
        self.assertListEqual(extract_index_list([1], [2], [1]), [])
        self.assertListEqual(extract_index_list([1], [1], [2]), [])
        self.assertListEqual(extract_index_list([1], [2], [3]), [])

    def test_multiple_elements(self):
        self.assertListEqual(extract_index_list([1, 1], [1, 1], [1, 1]), [1, 1])
        self.assertListEqual(extract_index_list([1, 2], [1, 2], [1, 2]), [1, 2])
        self.assertListEqual(extract_index_list([1, 1], [1, 2], [1, 1]), [1])
        self.assertListEqual(extract_index_list([1, 2], [1, 1], [1, 2]), [])
        self.assertListEqual(extract_index_list([1, 2], [2, 1], [1, 2]), [])

    def test_different_lengths(self):
        self.assertListEqual(extract_index_list([1, 1], [1, 1, 2], [1, 1]), [1, 1])
        self.assertListEqual(extract_index_list([1, 1], [1, 1, 2], [1, 2]), [])
        self.assertListEqual(extract_index_list([1, 1], [1, 1, 2], [1, 3]), [])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, extract_index_list, [1], 'a', [1])
        self.assertRaises(TypeError, extract_index_list, 'a', [1], [1])
        self.assertRaises(TypeError, extract_index_list, [1], [1], 'a')
