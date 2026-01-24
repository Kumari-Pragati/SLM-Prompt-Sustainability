import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 6)

    def test_single_number(self):
        self.assertEqual(big_diff([1]), 1)

    def test_empty_list(self):
        self.assertEqual(big_diff([]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(big_diff([1, -2, 3, -4, 5]), 7)
