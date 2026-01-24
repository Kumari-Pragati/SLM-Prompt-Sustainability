import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(modified_encode([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]), [[5, 5], [3, 3], [2, 2], [1], [4]])

    def test_edge_case_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(modified_encode([1]), [[1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1]), [[1, 1, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(modified_encode([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]), [[5, 5], [3, 3], [2, 2], [1], [4]])

    def test_edge_case_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(modified_encode([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]), [[5, 5], [3, 3], [2, 2], [1], [4]])
