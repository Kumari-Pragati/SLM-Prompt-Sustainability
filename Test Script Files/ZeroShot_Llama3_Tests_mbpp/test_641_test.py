import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_nonagonal_numbers(self):
        self.assertTrue(is_nonagonal(1))
        self.assertTrue(is_nonagonal(7))
        self.assertTrue(is_nonagonal(19))
        self.assertTrue(is_nonagonal(28))
        self.assertTrue(is_nonagonal(37))
        self.assertTrue(is_nonagonal(49))

    def test_non_nonagonal_numbers(self):
        self.assertFalse(is_nonagonal(0))
        self.assertFalse(is_nonagonal(2))
        self.assertFalse(is_nonagonal(3))
        self.assertFalse(is_nonagonal(4))
        self.assertFalse(is_nonagonal(5))
        self.assertFalse(is_nonagonal(6))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(TypeError):
            is_nonagonal(None)
        with self.assertRaises(TypeError):
            is_nonagonal(1.5)
