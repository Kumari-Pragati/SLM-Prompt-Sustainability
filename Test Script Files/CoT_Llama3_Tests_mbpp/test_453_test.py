import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):
    def test_sumofFactors_even(self):
        self.assertEqual(sumofFactors(12), 28)
    def test_sumofFactors_odd(self):
        self.assertEqual(sumofFactors(15), 0)
    def test_sumofFactors_prime(self):
        self.assertEqual(sumofFactors(7), 0)
    def test_sumofFactors_power_of_two(self):
        self.assertEqual(sumofFactors(8), 15)
    def test_sumofFactors_power_of_three(self):
        self.assertEqual(sumofFactors(27), 36)
    def test_sumofFactors_power_of_two_and_three(self):
        self.assertEqual(sumofFactors(36), 63)
    def test_sumofFactors_large_number(self):
        self.assertEqual(sumofFactors(100), 210)
