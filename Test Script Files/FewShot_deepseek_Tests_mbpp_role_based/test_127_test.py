import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_int(3, 4), 12)

    def test_zero_case(self):
        self.assertEqual(multiply_int(3, 0), 0)

    def test_negative_case(self):
        self.assertEqual(multiply_int(3, -4), -12)

    def test_negative_and_positive_case(self):
        self.assertEqual(multiply_int(-3, 4), -12)

    def test_one_case(self):
        self.assertEqual(multiply_int(3, 1), 3)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(100, 100), 10000)

    def test_large_negative_numbers(self):
        self.assertEqual(multiply_int(-100, -100), 10000)

    def test_large_negative_and_positive_numbers(self):
        self.assertEqual(multiply_int(-100, 100), -10000)
