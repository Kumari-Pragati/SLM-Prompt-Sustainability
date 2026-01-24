import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_dif_square_true(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(5))
        self.assertTrue(dif_Square(9))

    def test_dif_square_false(self):
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(6))
        self.assertFalse(dif_Square(10))
