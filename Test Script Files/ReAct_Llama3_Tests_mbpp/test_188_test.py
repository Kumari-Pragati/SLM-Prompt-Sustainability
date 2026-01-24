import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_true_positive(self):
        self.assertTrue(prod_Square(36))

    def test_true_negative(self):
        self.assertFalse(prod_Square(37))

    def test_edge_case(self):
        self.assertTrue(prod_Square(16))

    def test_edge_case_negative(self):
        self.assertFalse(prod_Square(17))

    def test_edge_case_zero(self):
        self.assertFalse(prod_Square(0))

    def test_edge_case_one(self):
        self.assertTrue(prod_Square(1))

    def test_edge_case_negative_one(self):
        self.assertFalse(prod_Square(-1))

    def test_edge_case_negative_zero(self):
        self.assertFalse(prod_Square(0))
