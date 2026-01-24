import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]), [[1], [2, 2], [3], [4, 4], [5], [6, 6], [7]])

    def test_edge_case_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1]), [[1, 1]])

    def test_edge_case_single_element_list_with_duplicates_and_non_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2]), [[1], [2, 2]])

    def test_edge_case_single_element_list_with_duplicates_and_non_duplicates_and_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 3]), [[1], [2, 2], [3, 3, 3]])

    def test_edge_case_single_element_list_with_duplicates_and_non_duplicates_and_duplicates_and_non_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]), [[1], [2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5, 5]])
