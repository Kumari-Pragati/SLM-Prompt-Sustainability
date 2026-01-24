import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(5, 7), 35)

    def test_zero(self):
        self.assertEqual(multiply_int(0, 0), 0)
        self.assertEqual(multiply_int(3, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_int(2, -3), -6)
        self.assertEqual(multiply_int(-5, -7), 35)

    def test_one(self):
        self.assertEqual(multiply_int(2, 1), 2)
        self.assertEqual(multiply_int(-2, 1), -2)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(100, 100), 10000)
        self.assertEqual(multiply_int(-100, 100), -10000)
