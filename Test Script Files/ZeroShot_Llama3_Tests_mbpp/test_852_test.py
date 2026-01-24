import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_remove_negs_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_remove_negs_all_positives(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_negs_all_negatives(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])

    def test_remove_negs_mixed_list(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_remove_negs_list_with_duplicates(self):
        self.assertEqual(remove_negs([1, -1, 2, -2, 3, -3]), [1, 2, 3])

    def test_remove_negs_list_with_duplicates_and_zero(self):
        self.assertEqual(remove_negs([1, -1, 2, -2, 0, -3]), [1, 2, 0, 3])
