import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_divisor_positive_numbers(self):
        self.assertEqual(divisor(12), 6)

    def test_divisor_zero(self):
        self.assertEqual(divisor(0), 1)

    def test_divisor_negative_numbers(self):
        self.assertEqual(divisor(-12), 3)

    def test_divisor_non_integer(self):
        self.assertEqual(divisor(12.5), 3)

    def test_divisor_edge_case(self):
        self.assertEqual(divisor(1), 1)

    def test_divisor_large_number(self):
        self.assertEqual(divisor(1000), 20)
