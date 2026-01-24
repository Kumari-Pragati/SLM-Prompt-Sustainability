import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(multiply_int(-2, 3), -6)
        self.assertEqual(multiply_int(2, -3), -6)

    def test_zero(self):
        self.assertEqual(multiply_int(2, 0), 0)
        self.assertEqual(multiply_int(0, 3), 0)
        self.assertEqual(multiply_int(0, 0), 0)

    def test_one(self):
        self.assertEqual(multiply_int(2, 1), 2)
        self.assertEqual(multiply_int(1, 2), 2)

    def test_large_numbers(self):
        self.assertEqual(multiply_int(100, 100), 10000)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(multiply_int(-2, 3), -6)
        self.assertEqual(multiply_int(2, -3), -6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_int('a', 2)
