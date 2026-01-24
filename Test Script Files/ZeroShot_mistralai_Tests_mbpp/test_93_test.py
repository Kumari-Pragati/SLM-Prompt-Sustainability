import unittest
from mbpp_93_code import power

class TestPowerFunction(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(power(2, 0), 1)

    def test_zero_base(self):
        self.assertEqual(power(0, 2), 0)

    def test_one_base(self):
        self.assertEqual(power(2, 1), 2)

    def test_simple_multiplication(self):
        self.assertEqual(power(2, 3), 8)

    def test_negative_exponent(self):
        self.assertEqual(power(2, -2), 1/4)

    def test_large_exponent(self):
        self.assertEqual(power(2, 10), 1024)
