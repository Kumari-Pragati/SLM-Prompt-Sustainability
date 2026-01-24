import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [1, 2, 3, 4])

    def test_edge_case_single_element(self):
        self.assertListEqual(extract_elements([1], 1), [1])

    def test_edge_case_empty_list(self):
        self.assertListEqual(extract_elements([], 1), [])

    def test_edge_case_single_element_group(self):
        self.assertListEqual(extract_elements([1, 1], 1), [1])

    def test_edge_case_multiple_element_group(self):
        self.assertListEqual(extract_elements([1, 1, 1], 1), [1])

    def test_edge_case_longer_group(self):
        self.assertListEqual(extract_elements([1, 1, 1, 2], 1), [1])

    def test_edge_case_shorter_group(self):
        self.assertListEqual(extract_elements([1, 1, 1, 1, 2], 2), [1, 1])

    def test_edge_case_zero_group(self):
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 2], 3), [1, 1, 1])

    def test_edge_case_negative_number(self):
        self.assertListEqual(extract_elements([-1, -1, 2, 2], 2), [])

    def test_edge_case_floats(self):
        self.assertListEqual(extract_elements([1.1, 1.1, 2.2, 2.2], 2), [1.1, 2.2])
