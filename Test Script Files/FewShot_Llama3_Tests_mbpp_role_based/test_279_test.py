import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_num_decagonal(1))
        self.assertTrue(is_num_decagonal(2))
        self.assertTrue(is_num_decagonal(3))

    def test_negative_numbers(self):
        self.assertFalse(is_num_decagonal(-1))
        self.assertFalse(is_num_decagonal(-2))
        self.assertFalse(is_num_decagonal(-3))

    def test_zero(self):
        self.assertFalse(is_num_decagonal(0))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_num_decagonal(1.5)
