import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_edge_case_single_element_set(self):
        self.assertEqual(extract_singly([[1, 1]]), [1])

    def test_edge_case_duplicates(self):
        self.assertEqual(extract_singly([[1, 2, 2, 3, 3, 3]]), [1, 2, 3])

    def test_edge_case_duplicates_with_duplicates(self):
        self.assertEqual(extract_singly([[1, 1, 2, 2, 3, 3, 3]]), [1, 2, 3])

    def test_edge_case_duplicates_with_duplicates_and_duplicates(self):
        self.assertEqual(extract_singly([[1, 1, 2, 2, 2, 3, 3, 3, 3]]), [1, 2, 3])

    def test_edge_case_duplicates_with_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(extract_singly([[1, 1, 1, 2, 2, 2, 3, 3, 3, 3]]), [1, 2, 3])

    def test_edge_case_duplicates_with_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(extract_singly([[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]]), [1, 2, 3])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            extract_singly("not a list")

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            extract_singly([1, 2, 3])

    def test_invalid_input_non_list_of_lists_of_lists(self):
        with self.assertRaises(TypeError):
            extract_singly([[[1, 2, 3]]])
