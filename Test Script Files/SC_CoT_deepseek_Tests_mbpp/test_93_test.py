import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_typical_case(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_with_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_with_zero_base(self):
        self.assertEqual(power(0, 3), 0)

    def test_power_with_one_exponent(self):
        self.assertEqual(power(2, 1), 2)

    def test_power_with_large_exponent(self):
        self.assertEqual(power(2, 10), 1024)

    def test_power_with_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)

    def test_power_with_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_with_negative_base_and_exponent(self):
        self.assertEqual(power(-2, -1), -0.5)
