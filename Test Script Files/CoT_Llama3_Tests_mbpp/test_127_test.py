import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_multiply_zero(self):
        self.assertEqual(multiply_int(2, 0), 0)

    def test_multiply_one(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_multiply_large(self):
        self.assertEqual(multiply_int(2, 100), 200)

    def test_multiply_negative_large(self):
        self.assertEqual(multiply_int(-2, 100), -200)

    def test_multiply_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_int('a', 2)

    def test_multiply_invalid_input2(self):
        with self.assertRaises(TypeError):
            multiply_int(2, 'b')
