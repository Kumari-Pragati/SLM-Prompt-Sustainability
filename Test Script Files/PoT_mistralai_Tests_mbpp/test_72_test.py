import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(16))
        self.assertFalse(dif_Square(20))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(dif_Square(2))
        self.assertFalse(dif_Square(0))
        self.assertFalse(dif_Square(3))
        self.assertFalse(dif_Square(5))
