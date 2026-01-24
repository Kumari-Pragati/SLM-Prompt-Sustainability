import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSum_of_Inverse_Divisors(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100), 10.0)

    def test_zero_divisor(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 0), 0.0)

    def test_zero_sum(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 0), 0.0)

    def test_negative_sum(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, -100), -10.0)

    def test_negative_divisor(self):
        self.assertEqual(Sum_of_Inverse_Divisors(-10, 100), -10.0)

    def test_non_integer_divisor(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100.5), 10.0)

    def test_non_integer_sum(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100.5), 10.0)
