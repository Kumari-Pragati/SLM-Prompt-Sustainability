import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):
    def test_true_odd(self):
        self.assertTrue(is_odd(3))

    def test_false_even(self):
        self.assertFalse(is_odd(4))

    def test_true_negative_odd(self):
        self.assertTrue(is_odd(-3))

    def test_false_negative_even(self):
        self.assertFalse(is_odd(-4))

    def test_true_zero(self):
        self.assertFalse(is_odd(0))

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            is_odd("hello")
