import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_dif_square_even_number(self):
        self.assertTrue(dif_Square(0))
        self.assertTrue(dif_Square(2))
        self.assertTrue(dif_Square(4))
        self.assertTrue(dif_Square(6))
        self.assertTrue(dif_Square(8))

    def test_dif_square_odd_number(self):
        self.assertFalse(dif_Square(1))
        self.assertFalse(dif_Square(3))
        self.assertFalse(dif_Square(5))
        self.assertFalse(dif_Square(7))
        self.assertFalse(dif_Square(9))

    def test_dif_square_four(self):
        self.assertFalse(dif_Square(4))
        self.assertTrue(dif_Square(5))
        self.assertTrue(dif_Square(6))
        self.assertFalse(dif_Square(7))
        self.assertTrue(dif_Square(8))
