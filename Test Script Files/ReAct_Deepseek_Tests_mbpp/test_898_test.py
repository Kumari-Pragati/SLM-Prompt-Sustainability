import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_typical_case(self):
        numbers = [1, 1, 2, 2, 2, 3, 3, 3, 3]
        n = 2
        result = extract_elements(numbers, n)
        self.assertEqual(result, [2, 3])

    def test_edge_case_single_element(self):
        numbers = [1]
        n = 1
        result = extract_elements(numbers, n)
        self.assertEqual(result, [1])

    def test_edge_case_empty_list(self):
        numbers = []
        n = 1
        result = extract_elements(numbers, n)
        self.assertEqual(result, [])

    def test_edge_case_n_greater_than_list_length(self):
        numbers = [1, 2, 3]
        n = 4
        result = extract_elements(numbers, n)
        self.assertEqual(result, [])

    def test_edge_case_n_equals_to_zero(self):
        numbers = [1, 2, 3]
        n = 0
        result = extract_elements(numbers, n)
        self.assertEqual(result, [])

    def test_typical_case_with_duplicates(self):
        numbers = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
        n = 3
        result = extract_elements(numbers, n)
        self.assertEqual(result, [3, 4])
