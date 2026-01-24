import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(7))

    def test_edge_cases(self):
        self.assertTrue(dif_Square(0))
        self.assertTrue(dif_Square(2))
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(6))
        self.assertFalse(dif_Square(8))

    def test_special_cases(self):
        self.assertTrue(dif_Square(72))
        self.assertFalse(dif_Square(74))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dif_Square('a')
        with self.assertRaises(TypeError):
            dif_Square(None)
        with self.assertRaises(TypeError):
            dif_Square([])
        with self.assertRaises(TypeError):
            dif_Square({})
