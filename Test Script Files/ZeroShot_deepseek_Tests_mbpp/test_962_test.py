import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_sum_Even_with_positive_numbers(self):
        self.assertEqual(sum_Even(1, 10), 25)
        self.assertEqual(sum_Even(1, 20), 110)
        self.assertEqual(sum_Even(1, 30), 240)

    def test_sum_Even_with_negative_numbers(self):
        self.assertEqual(sum_Even(-10, 10), 0)
        self.assertEqual(sum_Even(-20, 20), 0)

    def test_sum_Even_with_zero(self):
        self.assertEqual(sum_Even(0, 10), 25)
        self.assertEqual(sum_Even(0, 20), 110)

    def test_sum_Even_with_large_numbers(self):
        self.assertEqual(sum_Even(1, 1000000), 250000250000)
