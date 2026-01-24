import unittest
from mbpp_754_code import extract_index_list

class TestExtractIndexList(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1])

    def test_edge_case_empty_lists(self):
        self.assertEqual(extract_index_list([], [], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(extract_index_list([1], [1], [1]), [1])

    def test_edge_case_lists_of_length_one(self):
        self.assertEqual(extract_index_list([1], [2], [3]), [])

    def test_edge_case_lists_of_length_two(self):
        self.assertEqual(extract_index_list([1, 2], [1, 2], [1, 2]), [1, 2])

    def test_edge_case_lists_of_length_three(self):
        self.assertEqual(extract_index_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_edge_case_lists_of_length_four(self):
        self.assertEqual(extract_index_list([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]), [1, 2, 3, 4])

    def test_edge_case_lists_of_length_five(self):
        self.assertEqual(extract_index_list([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_index_list('a', [1, 2, 3], [1, 2, 3])

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            extract_index_list([1, 2], [1, 2, 3], [1, 2, 3])

    def test_invalid_input_length2(self):
        with self.assertRaises(IndexError):
            extract_index_list([1, 2, 3], [1, 2], [1, 2, 3])

    def test_invalid_input_length3(self):
        with self.assertRaises(IndexError):
            extract_index_list([1, 2, 3, 4], [1, 2], [1, 2, 3, 4])
