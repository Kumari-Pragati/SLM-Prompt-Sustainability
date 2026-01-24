import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(4))

    def test_edge_cases(self):
        self.assertTrue(dif_Square(0))
        self.assertFalse(dif_Square(-2))

    def test_boundary_conditions(self):
        self.assertTrue(dif_Square(7))
        self.assertFalse(dif_Square(8))
        self.assertTrue(dif_Square(9))
        self.assertFalse(dif_Square(10))
