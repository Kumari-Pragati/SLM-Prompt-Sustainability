import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):

    def test_sum_of_two_numbers(self):
        self.assertEqual(sum(12, 15), 3)

    def test_sum_of_prime_numbers(self):
        self.assertEqual(sum(7, 11), 1)

    def test_sum_of_numbers_with_common_divisor(self):
        self.assertEqual(sum(6, 12), 3)

    def test_sum_of_numbers_with_no_common_divisors(self):
        self.assertEqual(sum(10, 14), 0)

    def test_sum_of_zero_and_nonzero(self):
        self.assertEqual(sum(0, 10), 0)

    def test_sum_of_nonzero_and_zero(self):
        self.assertEqual(sum(10, 0), 0)

    def test_sum_of_negative_numbers(self):
        self.assertEqual(sum(-5, -7), 0)

    def test_sum_of_positive_and_negative(self):
        self.assertEqual(sum(5, -5), 0)

    def test_sum_of_zero(self):
        self.assertEqual(sum(0, 0), 0)

    def test_sum_of_nonzero(self):
        self.assertEqual(sum(5, 5), 0)
