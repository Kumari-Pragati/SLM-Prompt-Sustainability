import unittest
from72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_typical_input(self):
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(16))
        self.assertFalse(dif_Square(20))

    def test_edge_input(self):
        self.assertTrue(dif_Square(2))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(6))

    def test_boundary_input(self):
        self.assertFalse(dif_Square(0))
        self.assertTrue(dif_Square(1))
        self.assertFalse(dif_Square(5))

    def test_invalid_input(self):
        self.assertRaises(TypeError, dif_Square, 'string')
        self.assertRaises(TypeError, dif_Square, -1)
        self.assertRaises(TypeError, dif_Square, 2.5)
