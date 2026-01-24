import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_simple_even(self):
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(6))

    def test_simple_odd(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))

    def test_edge_0(self):
        self.assertTrue(dif_Square(0))

    def test_edge_1(self):
        self.assertFalse(dif_Square(1))

    def test_edge_3(self):
        self.assertFalse(dif_Square(3))

    def test_edge_negative(self):
        self.assertFalse(dif_Square(-1))
        self.assertFalse(dif_Square(-2))
        self.assertFalse(dif_Square(-3))

    def test_complex_4(self):
        self.assertFalse(dif_Square(4))

    def test_complex_16(self):
        self.assertFalse(dif_Square(16))
