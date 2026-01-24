import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_with_positive_base_and_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(5, 1), 5)

    def test_power_with_zero_base(self):
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)

    def test_power_with_zero_exponent(self):
        self.assertEqual(power(3, 0), 1)
        self.assertEqual(power(0, 3), 0)

    def test_power_with_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_with_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)
