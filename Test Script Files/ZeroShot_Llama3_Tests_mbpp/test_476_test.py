import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_negative_numbers(self):
        self.assertEqual(big_sum([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(big_sum([1, -2, 3]), 2)

    def test_single_number(self):
        self.assertEqual(big_sum([5]), 5)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            big_sum([])
