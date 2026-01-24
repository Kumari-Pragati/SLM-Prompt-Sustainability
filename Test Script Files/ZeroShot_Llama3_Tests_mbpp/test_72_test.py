import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):

    def test_true(self):
        self.assertTrue(dif_Square(10))

    def test_false(self):
        self.assertFalse(dif_Square(4))

    def test_edge_case(self):
        self.assertTrue(dif_Square(6))

    def test_edge_case2(self):
        self.assertFalse(dif_Square(8))

    def test_edge_case3(self):
        self.assertTrue(dif_Square(14))

    def test_edge_case4(self):
        self.assertFalse(dif_Square(12))
