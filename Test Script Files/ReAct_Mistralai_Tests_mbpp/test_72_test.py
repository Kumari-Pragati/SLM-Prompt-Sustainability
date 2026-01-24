import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_dif_square_positive_numbers(self):
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(16))
        self.assertFalse(dif_Square(20))
        self.assertFalse(dif_Square(24))
        self.assertFalse(dif_Square(28))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))
        self.assertTrue(dif_Square(7))
        self.assertTrue(dif_Square(9))

    def test_dif_square_zero(self):
        self.assertTrue(dif_Square(0))

    def test_dif_square_negative_numbers(self):
        self.assertTrue(dif_Square(-1))
        self.assertTrue(dif_Square(-2))
        self.assertTrue(dif_Square(-3))

    def test_dif_square_edge_cases(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(2))
        self.assertTrue(dif_Square(3))
