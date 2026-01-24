import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [2, 3, 4, 5])

    def test_edge_case_single_group(self):
        self.assertEqual(extract_elements([1, 1, 1, 1], 1), [1])

    def test_edge_case_single_group_empty(self):
        self.assertEqual(extract_elements([], 1), [])

    def test_edge_case_group_size_1(self):
        self.assertEqual(extract_elements([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_edge_case_group_size_1_empty(self):
        self.assertEqual(extract_elements([], 1), [])

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            extract_elements([1, 1, 1, 1], 'a')

    def test_invalid_input_non_list_numbers(self):
        with self.assertRaises(TypeError):
            extract_elements('abc', 1)

    def test_invalid_input_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            extract_elements([1.5, 2.5, 3.5], 1)
