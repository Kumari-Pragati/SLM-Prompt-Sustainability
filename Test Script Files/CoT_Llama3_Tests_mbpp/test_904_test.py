import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(even_num(4))
        self.assertTrue(even_num(10))
        self.assertTrue(even_num(20))

    def test_odd_numbers(self):
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(7))
        self.assertFalse(even_num(11))

    def test_edge_cases(self):
        self.assertTrue(even_num(0))
        self.assertFalse(even_num(-4))
        self.assertFalse(even_num(-10))

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            even_num('a')
        with self.assertRaises(TypeError):
            even_num(None)
