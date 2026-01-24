import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_edge_case_all_negatives(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])

    def test_edge_case_mixed_list(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_edge_case_single_negative(self):
        self.assertEqual(remove_negs([1, -2, 3]), [1, 3])

    def test_edge_case_single_positive(self):
        self.assertEqual(remove_negs([1]), [1])

    def test_edge_case_all_positives(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_negs([1, -1, 2, -2, 3, -3]), [1, 2, 3])

    def test_edge_case_duplicates_and_negatives(self):
        self.assertEqual(remove_negs([1, -1, 2, -2, 3, -3, 4, -4]), [1, 2, 3, 4])
