import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3, 3], 3), [3, 3, 3, 3])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_elements([], 3), [])

    def test_edge_case_single_element(self):
        self.assertEqual(extract_elements([1], 1), [1])
        self.assertEqual(extract_elements([1], 2), [])

    def test_boundary_case_minimum_value(self):
        self.assertEqual(extract_elements([1, 1, 1], 1), [1, 1, 1])

    def test_boundary_case_maximum_value(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3], 3), [3, 3, 3, 3, 3, 3])

    def test_complex_case_mixed_elements(self):
        self.assertEqual(extract_elements([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4], 4), [4, 4, 4, 4])

    def test_complex_case_multiple_groups(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4], 4), [4, 4, 4, 4])
