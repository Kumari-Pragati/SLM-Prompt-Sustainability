import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(even_num(4))

    def test_odd_number(self):
        self.assertFalse(even_num(5))

    def test_zero(self):
        self.assertTrue(even_num(0))

    def test_negative_number(self):
        self.assertTrue(even_num(-2))

    def test_large_positive_number(self):
        self.assertTrue(even_num(1000000))

    def test_large_negative_number(self):
        self.assertTrue(even_num(-1000000))
