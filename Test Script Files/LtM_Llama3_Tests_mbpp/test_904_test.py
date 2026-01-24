import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_simple_even(self):
        self.assertTrue(even_num(4))

    def test_simple_odd(self):
        self.assertFalse(even_num(3))

    def test_edge_zero(self):
        self.assertTrue(even_num(0))

    def test_edge_negative(self):
        self.assertTrue(even_num(-4))

    def test_edge_positive(self):
        self.assertTrue(even_num(4))

    def test_edge_zero_negative(self):
        self.assertTrue(even_num(0))

    def test_edge_zero_positive(self):
        self.assertTrue(even_num(0))

    def test_edge_negative_positive(self):
        self.assertTrue(even_num(-4))

    def test_edge_negative_negative(self):
        self.assertTrue(even_num(-4))

    def test_edge_positive_positive(self):
        self.assertTrue(even_num(4))

    def test_edge_negative_positive(self):
        self.assertTrue(even_num(-4))

    def test_edge_positive_negative(self):
        self.assertTrue(even_num(4))
