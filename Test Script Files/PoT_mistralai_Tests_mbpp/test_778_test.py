import unittest
from mbpp_778_code import pack_consecutive_duplicates

class TestPackConsecutiveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]), [
            [1, 1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5]
        ])

    def test_edge_case_single_element(self):
        self.assertEqual(pack_consecutive_duplicates([1]), [[1]])

    def test_edge_case_empty_list(self):
        self.assertEqual(pack_consecutive_duplicates([]), [])

    def test_edge_case_duplicate_first_element(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1]), [[1, 1]])

    def test_edge_case_duplicate_last_element(self):
        self.assertEqual(pack_consecutive_duplicates([1, 2, 2]), [[1], [2, 2]])

    def test_edge_case_only_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 1]), [[1, 1, 1]])

    def test_edge_case_consecutive_duplicates_and_non_duplicates(self):
        self.assertEqual(pack_consecutive_duplicates([1, 1, 2, 2, 3, 3]), [[1, 1], [2, 2], [3, 3]])
