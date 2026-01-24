import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [2, 4])

    def test_edge_case_n_zero(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 0), [])

    def test_edge_case_n_one(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 1), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_elements([], 2), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_elements([1], 2), [])

    def test_edge_case_single_element_list_n_one(self):
        self.assertEqual(extract_elements([1], 1), [1])

    def test_edge_case_single_element_list_n_zero(self):
        self.assertEqual(extract_elements([1], 0), [])

    def test_edge_case_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_elements('abc', 2)

    def test_edge_case_invalid_input_type_n_zero(self):
        with self.assertRaises(TypeError):
            extract_elements('abc', 0)
