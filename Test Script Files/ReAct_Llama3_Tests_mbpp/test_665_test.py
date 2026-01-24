import unittest
from mbpp_665_code import move_last

class TestMoveLast(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_edge_case_single_element(self):
        self.assertEqual(move_last([1]), [1])

    def test_edge_case_all_equal(self):
        self.assertEqual(move_last([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_edge_case_all_unique(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_last([]), [])

    def test_edge_case_list_with_one_occurrence(self):
        self.assertEqual(move_last([1, 2, 3, 4, 5, 1]), [2, 3, 4, 5, 1])

    def test_edge_case_list_with_multiple_occurrences(self):
        self.assertEqual(move_last([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
