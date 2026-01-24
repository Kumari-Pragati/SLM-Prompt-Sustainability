import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply_int(3, 4), 12)
        self.assertEqual(multiply_int(5, 0), 0)
        self.assertEqual(multiply_int(1, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_int(-3, -4), 12)
        self.assertEqual(multiply_int(-5, -0), 0)
        self.assertEqual(multiply_int(-1, -1), 1)

    def test_zero_multiplication(self):
        self.assertEqual(multiply_int(3, 0), 0)
        self.assertEqual(multiply_int(-3, 0), 0)

    def test_negative_multiplied_by_positive(self):
        self.assertEqual(multiply_int(3, -4), -12)
        self.assertEqual(multiply_int(-3, 4), -12)

    def test_positive_multiplied_by_negative(self):
        self.assertEqual(multiply_int(-3, -4), 12)
        self.assertEqual(multiply_int(3, -4), -12)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(1000000, 1000000), 1000000000000)
        self.assertEqual(multiply_int(-1000000, -1000000), 1000000000000)
