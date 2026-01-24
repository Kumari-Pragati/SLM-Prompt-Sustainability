import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_empty_list(self):
        self.assertEqual(consecutive_duplicates([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(consecutive_duplicates([1]), [1])

    def test_edge_case_duplicates_at_start(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 3, 4]), [1, 2, 3, 4])

    def test_edge_case_duplicates_at_end(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_in_middle(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_duplicates_everywhere(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_everywhere_reversed(self):
        self.assertEqual(consecutive_duplicates([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]), [1, 2, 3, 4, 5])
