import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):

    def test_sumofFactors_positive_even_numbers(self):
        self.assertEqual(sumofFactors(12), 18)
        self.assertEqual(sumofFactors(24), 30)
        self.assertEqual(sumofFactors(48), 72)

    def test_sumofFactors_positive_odd_numbers(self):
        self.assertEqual(sumofFactors(15), 0)
        self.assertEqual(sumofFactors(35), 0)
        self.assertEqual(sumofFactors(77), 0)

    def test_sumofFactors_zero(self):
        self.assertEqual(sumofFactors(0), 0)

    def test_sumofFactors_negative_numbers(self):
        self.assertEqual(sumofFactors(-12), 0)
        self.assertEqual(sumofFactors(-24), 0)
        self.assertEqual(sumofFactors(-48), 0)
