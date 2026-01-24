import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(consecutive_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 2, 3, 4, 4, 5])

    def test_edge_case_single_element(self):
        self.assertListEqual(consecutive_duplicates([1]), [1])

    def test_edge_case_empty_list(self):
        self.assertListEqual(consecutive_duplicates([]), [])

    def test_edge_case_duplicates_at_beginning(self):
        self.assertListEqual(consecutive_duplicates([2, 2, 1]), [2, 2])

    def test_edge_case_duplicates_at_end(self):
        self.assertListEqual(consecutive_duplicates([1, 2, 2]), [1, 2, 2])

    def test_edge_case_duplicates_only(self):
        self.assertListEqual(consecutive_duplicates([2, 2]), [2])

    def test_edge_case_duplicates_in_middle(self):
        self.assertListEqual(consecutive_duplicates([1, 2, 2, 2, 3]), [1, 2, 2])
