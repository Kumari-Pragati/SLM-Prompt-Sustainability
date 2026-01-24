import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sumofFactors(0), 0)

    def test_negative_number(self):
        self.assertEqual(sumofFactors(-1), 0)

    def test_one(self):
        self.assertEqual(sumofFactors(1), 1)

    def test_even_number(self):
        self.assertEqual(sumofFactors(2), 3)
        self.assertEqual(sumofFactors(4), 8)
        self.assertEqual(sumofFactors(10), 22)

    def test_odd_number(self):
        self.assertEqual(sumofFactors(3), 2)
        self.assertEqual(sumofFactors(5), 6)
        self.assertEqual(sumofFactors(9), 12)

    def test_prime_number(self):
        self.assertEqual(sumofFactors(7), 7)
        self.assertEqual(sumofFactors(11), 11)
        self.assertEqual(sumofFactors(13), 12)

    def test_composite_number(self):
        self.assertEqual(sumofFactors(6), 6)
        self.assertEqual(sumofFactors(8), 16)
        self.assertEqual(sumofFactors(12), 36)
        self.assertEqual(sumofFactors(15), 48)
        self.assertEqual(sumofFactors(18), 66)
