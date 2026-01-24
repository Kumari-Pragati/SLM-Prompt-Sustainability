import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_multiply_int_positive(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_multiply_int_negative(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_multiply_int_zero(self):
        self.assertEqual(multiply_int(2, 0), 0)

    def test_multiply_int_one(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_multiply_int_large(self):
        self.assertEqual(multiply_int(5, 10), 50)

    def test_multiply_int_negative_large(self):
        self.assertEqual(multiply_int(-5, 10), -50)

    def test_multiply_int_zero_large(self):
        self.assertEqual(multiply_int(5, 0), 0)

    def test_multiply_int_one_large(self):
        self.assertEqual(multiply_int(5, 1), 5)
