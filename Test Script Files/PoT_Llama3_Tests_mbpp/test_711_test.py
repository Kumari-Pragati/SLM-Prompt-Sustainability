import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(product_Equal(1234567890))

    def test_edge_case_n_10(self):
        self.assertFalse(product_Equal(10))

    def test_edge_case_n_9(self):
        self.assertFalse(product_Equal(9))

    def test_edge_case_n_0(self):
        self.assertFalse(product_Equal(0))

    def test_edge_case_n_negative(self):
        self.assertFalse(product_Equal(-1234567890))

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            product_Equal('1234567890')

    def test_edge_case_n_non_numeric(self):
        with self.assertRaises(TypeError):
            product_Equal([1234567890])

    def test_edge_case_n_non_integer_non_numeric(self):
        with self.assertRaises(TypeError):
            product_Equal({'1234567890'})
