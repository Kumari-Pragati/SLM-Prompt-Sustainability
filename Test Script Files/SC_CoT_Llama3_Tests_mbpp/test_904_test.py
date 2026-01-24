import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even(self):
        self.assertTrue(even_num(4))
        self.assertTrue(even_num(10))
        self.assertTrue(even_num(-4))

    def test_odd(self):
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(9))
        self.assertFalse(even_num(-3))

    def test_zero(self):
        self.assertTrue(even_num(0))

    def test_negative(self):
        self.assertTrue(even_num(-10))
        self.assertFalse(even_num(-3))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_num('a')

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            even_num([1, 2, 3])
