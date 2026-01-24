import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(even_num(4))
        self.assertTrue(even_num(10))
        self.assertTrue(even_num(20))

    def test_odd_numbers(self):
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(5))
        self.assertFalse(even_num(7))

    def test_zero(self):
        self.assertTrue(even_num(0))

    def test_negative_numbers(self):
        self.assertTrue(even_num(-4))
        self.assertTrue(even_num(-10))
        self.assertTrue(even_num(-20))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_num('a')
