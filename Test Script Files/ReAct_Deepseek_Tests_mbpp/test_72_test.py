import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(dif_Square(1))
        self.assertTrue(dif_Square(3))
        self.assertTrue(dif_Square(5))

    def test_edge_cases(self):
        self.assertTrue(dif_Square(0))
        self.assertFalse(dif_Square(2))
        self.assertFalse(dif_Square(4))
        self.assertFalse(dif_Square(6))

    def test_explicitly_handled_error_cases(self):
        self.assertRaises(TypeError, dif_Square, 'a')
        self.assertRaises(TypeError, dif_Square, None)
