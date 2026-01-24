import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_typical_input(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 3
        expected_output = [1, 2, 3, 4]
        self.assertEqual(extract_elements(numbers, n), expected_output)

    def test_edge_case_n_equal_to_length(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 12
        expected_output = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        self.assertEqual(extract_elements(numbers, n), expected_output)

    def test_edge_case_n_equal_to_zero(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 0
        expected_output = []
        self.assertEqual(extract_elements(numbers, n), expected_output)

    def test_edge_case_n_equal_to_one(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 1
        expected_output = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        self.assertEqual(extract_elements(numbers, n), expected_output)

    def test_special_case_n_greater_than_length(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 15
        expected_output = []
        self.assertEqual(extract_elements(numbers, n), expected_output)

    def test_invalid_input_non_integer(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = 'five'
        with self.assertRaises(TypeError):
            extract_elements(numbers, n)

    def test_invalid_input_negative(self):
        numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        n = -5
        with self.assertRaises(TypeError):
            extract_elements(numbers, n)
