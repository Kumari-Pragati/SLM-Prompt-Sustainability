import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(dif_Square(0))
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))

    def test_edge_conditions(self):
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(7))
        self.assertFalse(dif_Square(8))
        self.assertFalse(dif_Square(9))

    def test_complex_cases(self):
        self.assertTrue(dif_Square(4))
        self.assertTrue(dif_Square(5))
        self.assertTrue(dif_Square(6))
        self.assertFalse(dif_Square(10))
        self.assertFalse(dif_Square(11))
