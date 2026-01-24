import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(remove_negs([1, 2, 3]), [1, 2, 3])

    def test_simple_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -2, -3]), [])

    def test_mixed_numbers(self):
        self.assertEqual(remove_negs([-1, 2, -3, 4]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_single_negative_number(self):
        self.assertEqual(remove_negs([-1]), [])

    def test_single_positive_number(self):
        self.assertEqual(remove_negs([1]), [1])

    def test_all_zeroes(self):
        self.assertEqual(remove_negs([0, 0, 0]), [0, 0, 0])

    def test_mixed_with_zeroes(self):
        self.assertEqual(remove_negs([-1, 0, -2, 0, 3]), [0, 0, 3])
