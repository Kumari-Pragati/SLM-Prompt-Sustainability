import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):
    def test_zero_to_any_power(self):
        self.assertEqual(power(0, any_integer), 0)

    def test_one_to_any_power(self):
        self.assertEqual(power(1, any_integer), 1)

    def test_negative_base(self):
        self.assertEqual(power(-1, any_integer), 1 / power(1, any_integer))

    def test_negative_exponent(self):
        self.assertEqual(power(any_integer, -1), 1 / power(any_integer, 1))

    def test_zero_exponent(self):
        self.assertEqual(power(any_integer, 0), 1)

    def test_large_base_small_exponent(self):
        self.assertEqual(power(large_integer, small_integer), power(large_integer, small_integer) % prime_number)
