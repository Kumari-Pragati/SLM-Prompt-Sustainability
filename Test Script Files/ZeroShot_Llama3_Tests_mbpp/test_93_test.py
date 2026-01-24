import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_power_zero(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(0, 2), 0)

    def test_power_positive(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(2, 3), 8)

    def test_power_negative(self):
        self.assertEqual(power(-2, 0), 1)
        self.assertEqual(power(-2, 1), -2)
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)

    def test_power_non_integer(self):
        self.assertEqual(power(2.5, 0), 1)
        self.assertEqual(power(2.5, 1), 2.5)
        self.assertEqual(power(2.5, 2), 6.25)
        self.assertEqual(power(2.5, 3), 15.625)
