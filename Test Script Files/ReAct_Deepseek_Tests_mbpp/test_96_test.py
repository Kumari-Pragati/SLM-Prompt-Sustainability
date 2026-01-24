import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor_typical_cases(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(10), 4)

    def test_divisor_edge_cases(self):
        self.assertEqual(divisor(0), 1)  # 0 is a special case where it has only 1 divisor (itself)
        self.assertEqual(divisor(1), 1)  # 1 is a prime number with only 1 divisor
        self.assertEqual(divisor(997), 2)  # 997 is a prime number with only 2 divisors

    def test_divisor_error_cases(self):
        with self.assertRaises(TypeError):
            divisor('a')
        with self.assertRaises(ValueError):
            divisor(-1)
