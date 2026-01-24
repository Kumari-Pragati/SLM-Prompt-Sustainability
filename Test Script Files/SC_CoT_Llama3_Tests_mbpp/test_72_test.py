import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(dif_Square(10))

    def test_edge_case(self):
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(8))
        self.assertFalse(dif_Square(12))

    def test_boundary_case(self):
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))
        self.assertTrue(dif_Square(7))

    def test_special_case(self):
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(6))
        self.assertFalse(dif_Square(10))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dif_Square('a')
