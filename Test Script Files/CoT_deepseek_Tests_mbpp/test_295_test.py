import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(sum_div(10), 1+2+5)

    def test_prime_number(self):
        self.assertEqual(sum_div(7), 1)

    def test_number_with_no_divisors_other_than_1(self):
        self.assertEqual(sum_div(1), 1)

    def test_number_with_divisors_other_than_1(self):
        self.assertEqual(sum_div(12), 1+2+3+4+6)

    def test_large_number(self):
        self.assertEqual(sum_div(100), 1+2+4+5+10+20+25+50)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            sum_div(-10)

    def test_zero(self):
        with self.assertRaises(Exception):
            sum_div(0)
