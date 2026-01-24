import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_even_num_returns_true_for_even_numbers(self):
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(4))
        self.assertTrue(even_num(10))

    def test_even_num_returns_false_for_odd_numbers(self):
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(5))
