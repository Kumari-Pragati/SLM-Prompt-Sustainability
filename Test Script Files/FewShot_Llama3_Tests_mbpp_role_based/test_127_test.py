import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_int(-2, -3), 6)

    def test_multiply_zero(self):
        self.assertEqual(multiply_int(0, 0), 0)

    def test_multiply_one(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply_int(100, 200), 20000)

    def test_multiply_negative_and_positive_numbers(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_multiply_negative_and_negative_numbers(self):
        self.assertEqual(multiply_int(-2, -3), 6)
