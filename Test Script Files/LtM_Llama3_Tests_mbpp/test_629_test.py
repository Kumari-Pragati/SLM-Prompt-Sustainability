import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_even(self):
        self.assertEqual(Split([2]), [2])

    def test_single_odd(self):
        self.assertEqual(Split([3]), [])

    def test_multiple_evens(self):
        self.assertEqual(Split([2, 4, 6]), [2, 4, 6])

    def test_multiple_odds(self):
        self.assertEqual(Split([1, 3, 5]), [])

    def test_mixed_list(self):
        self.assertEqual(Split([2, 3, 4, 5, 6]), [2, 4, 6])

    def test_negative_numbers(self):
        self.assertEqual(Split([-2, -4, -6]), [-2, -4, -6])

    def test_zero(self):
        self.assertEqual(Split([0]), [0])
