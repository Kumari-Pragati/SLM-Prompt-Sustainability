import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 3], 2), [1, 2, 3])

    def test_edge_case_n_equals_one(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 3], 1), [1, 1, 2, 2, 3, 3, 3])

    def test_edge_case_n_equals_length(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3, 3], 7), [])

    def test_corner_case_empty_list(self):
        self.assertEqual(extract_elements([], 2), [])

    def test_invalid_input_n_less_than_one(self):
        with self.assertRaises(ValueError):
            extract_elements([1, 1, 2, 2, 3, 3, 3], 0)

    def test_invalid_input_n_greater_than_length(self):
        with self.assertRaises(ValueError):
            extract_elements([1, 1, 2, 2, 3, 3, 3], 8)
