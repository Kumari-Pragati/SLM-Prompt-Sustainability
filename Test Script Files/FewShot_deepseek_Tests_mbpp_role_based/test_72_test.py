import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(dif_Square(4))
        self.assertFalse(dif_Square(5))

    def test_boundary_conditions(self):
        self.assertTrue(dif_Square(0))
        self.assertFalse(dif_Square(2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dif_Square('a')
