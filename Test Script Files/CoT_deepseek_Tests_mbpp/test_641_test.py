import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 10)
        self.assertEqual(is_nonagonal(3), 22)
        self.assertEqual(is_nonagonal(4), 37)

    def test_negative_numbers(self):
        self.assertEqual(is_nonagonal(-1), -1)
        self.assertEqual(is_nonagonal(-2), -10)
        self.assertEqual(is_nonagonal(-3), -22)
        self.assertEqual(is_nonagonal(-4), -37)

    def test_zero(self):
        self.assertEqual(is_nonagonal(0), 0)

    def test_large_numbers(self):
        self.assertEqual(is_nonagonal(100), 3975)
        self.assertEqual(is_nonagonal(200), 19900)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_nonagonal("invalid")
