import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(0))

    def test_boundary_conditions(self):
        self.assertTrue(dif_Square(-1))
        self.assertFalse(dif_Square(-2))
        self.assertTrue(dif_Square(4))
        self.assertFalse(dif_Square(6))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            dif_Square('a')
        with self.assertRaises(TypeError):
            dif_Square(None)
        with self.assertRaises(TypeError):
            dif_Square([])
