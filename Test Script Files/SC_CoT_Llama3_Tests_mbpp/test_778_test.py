import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 5]), [[1], [2, 2], [3, 3, 3], [4], [5, 5]])

    def test_edge_case_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1]), [[1, 1]])

    def test_edge_case_all_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1, 1, 1]), [[1, 1, 1, 1, 1]])

    def test_edge_case_all_unique(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 3, 4, 5]), [[1], [2], [3], [4], [5]])

    def test_edge_case_mixed_duplicates_and_unique(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 5, 6]), [[1], [2, 2], [3, 3, 3], [4], [5, 5], [6]])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            pack_consecutive_duplicates("hello")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            pack_consecutive_duplicates(123)
