import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(5, 7), 35)
        self.assertEqual(multiply_int(10, 0), 0)
        self.assertEqual(multiply_int(1, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_int(-2, -3), 6)
        self.assertEqual(multiply_int(-5, -7), 35)
        self.assertEqual(multiply_int(-10, -0), 0)
        self.assertEqual(multiply_int(-1, -1), 1)

    def test_zero(self):
        self.assertEqual(multiply_int(0, 2), 0)
        self.assertEqual(multiply_int(2, 0), 0)

    def test_one(self):
        self.assertEqual(multiply_int(1, 1), 1)
        self.assertEqual(multiply_int(2, 1), 2)
        self.assertEqual(multiply_int(-1, 1), -1)
        self.assertEqual(multiply_int(-2, 1), -2)

    def test_edge_cases(self):
        self.assertEqual(multiply_int(1, -2147483648), 2147483648)
        self.assertEqual(multiply_int(-1, 2147483648), -2147483648)
