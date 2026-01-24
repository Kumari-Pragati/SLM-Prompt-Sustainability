import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(0))
        self.assertFalse(even_num(1))

    def test_edge_cases(self):
        self.assertTrue(even_num(-4))
        self.assertFalse(even_num(-1))

    def test_boundary_cases(self):
        self.assertTrue(even_num(2**31))
        self.assertFalse(even_num(2**31 - 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_num(None)
        with self.assertRaises(TypeError):
            even_num('string')
        with self.assertRaises(TypeError):
            even_num([])
