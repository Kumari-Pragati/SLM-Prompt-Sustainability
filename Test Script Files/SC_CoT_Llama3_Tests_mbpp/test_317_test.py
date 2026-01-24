import unittest
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(modified_encode([1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]), [[2, 1], [1, 2], [3, 3], [1, 4], [4, 5]])

    def test_edge_case_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(modified_encode([1]), [[1, 1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1]), [[3, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1]), [[4, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1]), [[5, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1]), [[6, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1]), [[7, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1]), [[8, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1]), [[9, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[10, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[11, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[12, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[13, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[14, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [[15, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(modified_encode([1, 1, 1, 1, 1, 1, 1, 1