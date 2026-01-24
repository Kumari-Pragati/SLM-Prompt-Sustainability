import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_nonagonal(10))

    def test_edge_case(self):
        self.assertFalse(is_nonagonal(0))
        self.assertFalse(is_nonagonal(1))
        self.assertFalse(is_nonagonal(2))
        self.assertFalse(is_nonagonal(3))
        self.assertFalse(is_nonagonal(4))
        self.assertFalse(is_nonagonal(5))
        self.assertFalse(is_nonagonal(6))

    def test_nonagonal_numbers(self):
        self.assertTrue(is_nonagonal(7))
        self.assertTrue(is_nonagonal(12))
        self.assertTrue(is_nonagonal(17))
        self.assertTrue(is_nonagonal(22))
        self.assertTrue(is_nonagonal(27))

    def test_non_nonagonal_numbers(self):
        self.assertFalse(is_nonagonal(8))
        self.assertFalse(is_nonagonal(9))
        self.assertFalse(is_nonagonal(11))
        self.assertFalse(is_nonagonal(13))
        self.assertFalse(is_nonagonal(14))
        self.assertFalse(is_nonagonal(15))
        self.assertFalse(is_nonagonal(16))
        self.assertFalse(is_nonagonal(18))
        self.assertFalse(is_nonagonal(19))
        self.assertFalse(is_nonagonal(20))
        self.assertFalse(is_nonagonal(21))
        self.assertFalse(is_nonagonal(23))
        self.assertFalse(is_nonagonal(24))
        self.assertFalse(is_nonagonal(25))
        self.assertFalse(is_nonagonal(26))
        self.assertFalse(is_nonagonal(28))
        self.assertFalse(is_nonagonal(29))
        self.assertFalse(is_nonagonal(30))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
        with self.assertRaises(TypeError):
            is_nonagonal(None)
        with self.assertRaises(TypeError):
            is_nonagonal(10.5)
