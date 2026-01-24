import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor_positive_integer(self):
        self.assertEqual(divisor(12), 6)
        self.assertEqual(divisor(2), 1)
        self.assertEqual(divisor(4), 2)

    def test_divisor_zero(self):
        self.assertEqual(divisor(0), 0)

    def test_divisor_negative_integer(self):
        self.assertEqual(divisor(-1), 0)
        self.assertEqual(divisor(-2), 1)
        self.assertEqual(divisor(-12), 6)

    def test_divisor_one(self):
        self.assertEqual(divisor(1), 0)

    def test_divisor_large_number(self):
        self.assertEqual(divisor(1000000), 1000000)

    def test_divisor_small_number(self):
        self.assertEqual(divisor(1), 0)

    def test_divisor_non_integer(self):
        self.assertRaises(TypeError, divisor, 3.14)
