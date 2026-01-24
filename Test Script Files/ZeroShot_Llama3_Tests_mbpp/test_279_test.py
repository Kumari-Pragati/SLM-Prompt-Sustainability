import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_is_num_decagonal_positive(self):
        self.assertTrue(is_num_decagonal(1))
        self.assertTrue(is_num_decagonal(2))
        self.assertTrue(is_num_Decagonal(3))

    def test_is_num_decagonal_negative(self):
        self.assertFalse(is_num_decagonal(-1))
        self.assertFalse(is_num_decagonal(-2))
        self.assertFalse(is_num_decagonal(-3))

    def test_is_num_decagonal_zero(self):
        self.assertFalse(is_num_decagonal(0))

    def test_is_num_decagonal_non_integer(self):
        with self.assertRaises(TypeError):
            is_num_decagonal(1.5)

    def test_is_num_decagonal_non_numeric(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
