import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(-2, 0), 1)

    def test_power_one_exponent(self):
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(-2, 1), -2)

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(10, 4), 10000)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(3, -2), 1/9)
        self.assertAlmostEqual(power(10, -3), 0.001)
