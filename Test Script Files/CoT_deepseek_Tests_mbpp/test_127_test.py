import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_negative_y(self):
        self.assertEqual(multiply_int(2, -3), -6)

    def test_zero_y(self):
        self.assertEqual(multiply_int(2, 0), 0)

    def test_one_y(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(100, 100), 10000)

    def test_negative_x(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_negative_x_and_y(self):
        self.assertEqual(multiply_int(-2, -3), 6)
