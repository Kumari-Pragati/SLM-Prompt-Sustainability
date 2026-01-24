import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_negative_numbers(self):
        self.assertEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(larg_nnum([-1, 2, -3, 4, -5], 3), [4, 2, -1])

    def test_duplicate_numbers(self):
        self.assertEqual(larg_nnum([5, 5, 5, 5, 5], 3), [5, 5, 5])

    def test_large_n(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_empty_list(self):
        self.assertEqual(larg_nnum([], 3), [])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3, 4, 5], -1)
