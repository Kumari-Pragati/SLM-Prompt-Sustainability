import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_num_typical(self):
        self.assertTrue(even_num(4))

    def test_even_num_odd(self):
        self.assertFalse(even_num(3))

    def test_even_num_zero(self):
        self.assertTrue(even_num(0))

    def test_even_num_negative(self):
        self.assertTrue(even_num(-4))

    def test_even_num_non_integer(self):
        with self.assertRaises(TypeError):
            even_num('a')
