import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_all_positive(self):
        self.assertEqual(remove_negs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])

    def test_mixed_list(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_single_negative(self):
        self.assertEqual(remove_negs([1, -2, 3, 4, 5]), [1, 3, 4, 5])

    def test_single_positive(self):
        self.assertEqual(remove_negs([-1, 2, -3, 4, -5]), [2, 4])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_negs([1, -2, 2, -3, 3]), [1, 2, 3])

    def test_list_with_duplicates_and_negative(self):
        self.assertEqual(remove_negs([-1, -2, 2, -3, 3, 4, -5]), [2, 3, 4])
