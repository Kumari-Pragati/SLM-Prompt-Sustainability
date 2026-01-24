import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_num_positive(self):
        self.assertTrue(even_num(0))
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(100))

    def test_even_num_negative(self):
        self.assertFalse(even_num(-1))
        self.assertFalse(even_num(-2))
        self.assertFalse(even_num(-100))

    def test_even_num_zero(self):
        self.assertTrue(even_num(0))

    def test_even_num_boundary(self):
        self.assertTrue(even_num(1))
        self.assertFalse(even_num(2))
