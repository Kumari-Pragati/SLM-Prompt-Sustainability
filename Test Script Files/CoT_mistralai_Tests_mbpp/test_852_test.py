import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_negs([]), [])

    def test_positive_list(self):
        self.assertListEqual(remove_negs([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_mixed_list(self):
        self.assertListEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_single_negative(self):
        self.assertListEqual(remove_negs([-1]), [])

    def test_multiple_negatives(self):
        self.assertListEqual(remove_negs([-1, -2, -3]), [])

    def test_zero(self):
        self.assertListEqual(remove_negs([0]), [0])

    def test_large_positive_numbers(self):
        self.assertListEqual(remove_negs([1000000, 2000000, -3000000]), [1000000, 2000000])

    def test_large_negative_numbers(self):
        self.assertListEqual(remove_negs([-1000000, -2000000, 3000000]), [3000000])

    def test_float_positive(self):
        self.assertListEqual(remove_negs([1.1, -2.2, 3.3]), [1.1, 3.3])

    def test_float_negative(self):
        self.assertListEqual(remove_negs([-1.1, 2.2, -3.3]), [])
