import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_all_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -2, -3, -4]), [])

    def test_all_positive_numbers(self):
        self.assertEqual(remove_negs([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_mixed_numbers(self):
        self.assertEqual(remove_negs([-1, 0, 1, -2, 2]), [0, 1, 2])

    def test_duplicates(self):
        self.assertEqual(remove_negs([-1, -1, 0, 1, 1]), [0])

    def test_single_negative_number(self):
        self.assertEqual(remove_negs([-1]), [])

    def test_single_positive_number(self):
        self.assertEqual(remove_negs([1]), [1])

    def test_zero(self):
        self.assertEqual(remove_negs([0]), [0])
