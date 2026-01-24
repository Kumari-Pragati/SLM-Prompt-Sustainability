import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1])

    def test_edge_case_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(extract_index_list([1], [1], [1]), [1])

    def test_edge_case_all_elements_equal(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 1, 1], [1, 1, 1]), [1])

    def test_edge_case_all_elements_not_equal(self):
        self.assertEqual(extract_index_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [])

    def test_edge_case_mixed_elements(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 3, 2], [1, 2, 3]), [1])

    def test_edge_case_repeated_elements(self):
        self.assertEqual(extract_index_list([1, 1, 1], [1, 2, 3], [1, 1, 1]), [1])

    def test_edge_case_invalid_input_types(self):
        with self.assertRaises(TypeError):
            extract_index_list('a', [1, 2, 3], [1, 2, 3])

    def test_edge_case_invalid_input_lengths(self):
        with self.assertRaises(IndexError):
            extract_index_list([1, 2], [1, 2, 3], [1, 2, 3])
