import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remove_negs([1, 2, -3, 4, -5]), [1, 2, 4])

    def test_empty_list(self):
        self.assertEqual(remove_negs([]), [])

    def test_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -2, -3]), [])

    def test_single_negative_number(self):
        self.assertEqual(remove_negs([0, -1]), [0])

    def test_duplicate_negative_numbers(self):
        self.assertEqual(remove_negs([-1, -1, 0, 1]), [0, 1])
