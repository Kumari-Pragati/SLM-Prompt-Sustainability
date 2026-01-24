import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_singly([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_singly([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_singly([[1]]), [1])

    def test_edge_case_single_element_set(self):
        self.assertEqual(extract_singly([[1, 1]]), [1])

    def test_edge_case_duplicates(self):
        self.assertEqual(extract_singly([[1, 1, 2, 2, 3, 3]]), [1, 2, 3])

    def test_edge_case_empty_inner_list(self):
        self.assertEqual(extract_singly([[], []]), [])

    def test_edge_case_single_empty_inner_list(self):
        self.assertEqual(extract_singly([[], [1]]), [1])

    def test_edge_case_multiple_empty_inner_lists(self):
        self.assertEqual(extract_singly([[], [], []]), [])

    def test_edge_case_single_empty_inner_list_with_duplicates(self):
        self.assertEqual(extract_singly([[], [1, 1]]), [1])
