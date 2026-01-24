import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_num(self):
        self.assertTrue(even_num(4))
        self.assertTrue(even_num(10))
        self.assertTrue(even_num(20))

        self.assertFalse(even_num(1))
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(5))

        self.assertTrue(even_num(0))
