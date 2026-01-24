import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_all_positive_numbers(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])

    def test_mixed_numbers(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_negs([-1, -1, 1, 2, -3]), [1, 2])

    def test_list_with_negative_and_positive_duplicates(self):
        self.assertEqual(remove_negs([-1, -1, 1, 1, 2, -3, 3]), [1, 1, 2, 3])
