import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_big_diff_positive_numbers(self):
        self.assertEqual(big_diff([10, 2, 7, 2]), 8)

    def test_big_diff_negative_numbers(self):
        self.assertEqual(big_diff([10, 2, -7, 2]), 19)

    def test_big_diff_mixed_numbers(self):
        self.assertEqual(big_diff([-10, 2, 7, -2]), 19)

    def test_big_diff_single_number(self):
        self.assertEqual(big_diff([1]), 0)

    def test_big_diff_empty_list(self):
        with self.assertRaises(ValueError):
            big_diff([])
