import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(0))
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(-1))

    def test_edge_cases(self):
        self.assertTrue(even_num(2**64 - 2))  # Max even number in a 64-bit system
        self.assertFalse(even_num(2**64 - 1))  # Max odd number in a 64-bit system

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            even_num('a')
        with self.assertRaises(TypeError):
            even_num(None)
