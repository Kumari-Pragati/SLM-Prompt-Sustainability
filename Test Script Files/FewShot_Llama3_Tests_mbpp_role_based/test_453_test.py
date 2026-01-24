import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):
    def test_sumofFactors_positive_integer(self):
        self.assertEqual(sumofFactors(12), 28)

    def test_sumofFactors_perfect_square(self):
        self.assertEqual(sumofFactors(36), 60)

    def test_sumofFactors_perfect_cube(self):
        self.assertEqual(sumofFactors(27), 60)

    def test_sumofFactors_prime_number(self):
        self.assertEqual(sumofFactors(23), 0)

    def test_sumofFactors_even_number(self):
        self.assertEqual(sumofFactors(20), 66)

    def test_sumofFactors_zero(self):
        self.assertEqual(sumofFactors(0), 1)

    def test_sumofFactors_negative_number(self):
        with self.assertRaises(TypeError):
            sumofFactors(-1)
