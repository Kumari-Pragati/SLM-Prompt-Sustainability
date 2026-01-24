import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_even_num(self):
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(0))
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(-1))
        self.assertFalse(even_num(-3))
