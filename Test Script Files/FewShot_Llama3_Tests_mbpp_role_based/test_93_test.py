import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_power_of_zero(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_of_nonzero(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_of_one(self):
        self.assertEqual(power(2, 1), 2)

    def test_power_of_negative(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_of_zero_base(self):
        self.assertEqual(power(0, 0), 1)

    def test_power_of_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_of_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_of_negative_exponent(self):
        self.assertEqual(power(-2, -3), 1/8)

    def test_power_of_noninteger_base(self):
        self.assertEqual(power(2.5, 3), 15.625)

    def test_power_of_noninteger_exponent(self):
        self.assertEqual(power(2, 3.5), 11.3137)
