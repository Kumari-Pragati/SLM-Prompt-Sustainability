import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3], 2), [1, 2, 3])

    def test_edge_case_n_equals_1(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3], 1), [1, 1, 2, 2, 3, 3])

    def test_boundary_case_n_equals_0(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3], 0), [])

    def test_corner_case_empty_list(self):
        self.assertEqual(extract_elements([], 2), [])

    def test_corner_case_n_greater_than_length(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3], 7), [])

    def test_corner_case_n_equals_length(self):
        self.assertEqual(extract_elements([1, 1, 2, 2, 3, 3], 6), [])
