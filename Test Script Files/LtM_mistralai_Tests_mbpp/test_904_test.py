import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_simple_even(self):
        self.assertTrue(even_num(0))
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(100))

    def test_simple_odd(self):
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(201))

    def test_edge_cases(self):
        self.assertTrue(even_num(-2))
        self.assertTrue(even_num(2147483646))  # max int value
        self.assertFalse(even_num(-2147483647))  # min int value

    def test_complex_cases(self):
        self.assertTrue(even_num(-100))
        self.assertFalse(even_num(2147483649))  # odd number just above max int value
        self.assertRaises(TypeError, even_num, 'a')  # string input
