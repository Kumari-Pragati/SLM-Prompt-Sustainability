import unittest
from mbpp_93_code import power

class TestPower(unittest.TestCase):
    def test_power_zero(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(0, 2), 0)

    def test_power_one(self):
        self.assertEqual(power(1, 0), 1)
        self.assertEqual(power(1, 1), 1)
        self.assertEqual(power(1, 2), 1)

    def test_power_nonzero(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 2), 4)

    def test_power_negative(self):
        self.assertEqual(power(-2, 0), 1)
        self.assertEqual(power(-2, 1), -2)
        self.assertEqual(power(-2, 2), 4)

    def test_power_noninteger(self):
        self.assertEqual(power(2.5, 0), 1)
        self.assertEqual(power(2.5, 1), 2.5)
        self.assertEqual(power(2.5, 2), 6.25)
