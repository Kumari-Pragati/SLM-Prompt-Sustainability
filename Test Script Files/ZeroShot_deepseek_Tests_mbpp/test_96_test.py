import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor_positive_numbers(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(10), 4)

    def test_divisor_zero(self):
        self.assertEqual(divisor(0), 1)

    def test_divisor_negative_numbers(self):
        self.assertEqual(divisor(-1), 1)
        self.assertEqual(divisor(-2), 2)
        self.assertEqual(divisor(-4), 3)
        self.assertEqual(divisor(-10), 4)
