import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_sum_digits_twoparts_positive_numbers(self):
        test_cases = [(12, 12), (100, 19), (999, 99), (1000, 1)]
        for num, expected in test_cases:
            with self.subTest(f"Testing sum_digits_twoparts({num})"):
                self.assertEqual(sum_digits_twoparts(num), expected)

    def test_sum_digits_twoparts_zero(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_sum_digits_twoparts_negative_numbers(self):
        test_cases = [(-12, 12), (-100, 19), (-999, 99), (-1000, 1)]
        for num, expected in test_cases:
            with self.subTest(f"Testing sum_digits_twoparts({num})"):
                self.assertEqual(sum_digits_twoparts(num), expected)

    def test_sum_digits_twoparts_large_numbers(self):
        test_cases = [(10**5, 1 + 9 * 5), (10**6, 1 + 9 * 6), (10**7, 1 + 9 * 7)]
        for num, expected in test_cases:
            with self.subTest(f"Testing sum_digits_twoparts({num})"):
                self.assertEqual(sum_digits_twoparts(num), expected)
