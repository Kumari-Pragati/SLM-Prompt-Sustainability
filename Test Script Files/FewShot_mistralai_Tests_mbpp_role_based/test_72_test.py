import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_valid_positive_numbers(self):
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(16))
        self.assertFalse(dif_Square(20))

    def test_valid_negative_numbers(self):
        self.assertFalse(dif_Square(-4))
        self.assertFalse(dif_Square(-16))
        self.assertFalse(dif_Square(-20))

    def test_zero(self):
        self.assertTrue(dif_Square(0))

    def test_non_square_numbers(self):
        self.assertTrue(dif_Square(9))
        self.assertTrue(dif_Square(25))
        self.assertTrue(dif_Square(100))
