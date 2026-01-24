import unittest
from mbpp_179_code import is_num_keith

class TestIsNumKeith(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_num_keith(123))
        self.assertTrue(is_num_keith(456))
        self.assertTrue(is_num_keith(789))

    def test_zero(self):
        self.assertFalse(is_num_keith(0))

    def test_single_digit(self):
        self.assertFalse(is_num_keith(1))
        self.assertFalse(is_num_keith(2))
        self.assertFalse(is_num_keith(3))

    def test_edge_case(self):
        self.assertFalse(is_num_keith(1234567890))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_num_keith('abc')

    def test_negative_input(self):
        self.assertFalse(is_num_keith(-123))

    def test_large_input(self):
        self.assertFalse(is_num_keith(1234567890123456789))
