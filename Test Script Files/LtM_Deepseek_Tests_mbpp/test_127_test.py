import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_multiply_simple(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(5, 4), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_int(2, 0), 0)
        self.assertEqual(multiply_int(-3, 0), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply_int(2, 1), 2)
        self.assertEqual(multiply_int(-3, 1), -3)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_int(-2, -3), 6)
        self.assertEqual(multiply_int(2, -3), -6)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply_int(1000, 1000), 1000000)
