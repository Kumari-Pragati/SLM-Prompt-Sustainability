import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_positive_base_and_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 4), 81)

    def test_zero_base_and_exponent(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)

    def test_negative_base_and_exponent(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-3, 4), -81)

    def test_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)
        self.assertEqual(power(-2, -3), -0.125)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(power(2, 0.5), 1.4142135623730951)
        self.assertAlmostEqual(power(-2, 0.5), -1.4142135623730951)
