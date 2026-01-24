import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_zero_multiplication(self):
        self.assertEqual(multiply_int(0, 0), 0)
        self.assertEqual(multiply_int(5, 0), 0)
        self.assertEqual(multiply_int(-3, 0), 0)

    def test_one_multiplication(self):
        self.assertEqual(multiply_int(3, 1), 3)
        self.assertEqual(multiply_int(-5, 1), -5)

    def test_negative_multiplication(self):
        self.assertEqual(multiply_int(3, -2), -6)
        self.assertEqual(multiply_int(-5, -3), 15)

    def test_large_multiplication(self):
        self.assertEqual(multiply_int(7, 10), 70)
        self.assertEqual(multiply_int(-3, 12), -36)
