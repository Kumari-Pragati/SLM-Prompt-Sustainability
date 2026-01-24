import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_true_output(self):
        self.assertTrue(prod_Square(36))

    def test_false_output(self):
        self.assertFalse(prod_Square(5))

    def test_edge_case(self):
        self.assertTrue(prod_Square(16))

    def test_edge_case2(self):
        self.assertFalse(prod_Square(17))

    def test_edge_case3(self):
        self.assertFalse(prod_Square(0))

    def test_edge_case4(self):
        self.assertFalse(prod_Square(-1))

    def test_edge_case5(self):
        self.assertFalse(prod_Square(1))
