import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_true(self):
        self.assertTrue(prod_Square(36))

    def test_false(self):
        self.assertFalse(prod_Square(5))

    def test_edge_case(self):
        self.assertFalse(prod_Square(1))

    def test_edge_case2(self):
        self.assertTrue(prod_Square(4))

    def test_edge_case3(self):
        self.assertFalse(prod_Square(3))

    def test_edge_case4(self):
        self.assertFalse(prod_Square(2))

    def test_edge_case5(self):
        self.assertFalse(prod_Square(0))

    def test_edge_case6(self):
        self.assertFalse(prod_Square(-1))

    def test_edge_case7(self):
        self.assertFalse(prod_Square(-2))

    def test_edge_case8(self):
        self.assertFalse(prod_Square(-3))

    def test_edge_case9(self):
        self.assertFalse(prod_Square(-4))

    def test_edge_case10(self):
        self.assertFalse(prod_Square(-5))
