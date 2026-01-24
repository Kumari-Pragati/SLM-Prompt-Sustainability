import unittest
from mbpp_72_code import dif_Square

class TestDifSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(dif_Square(10))

    def test_edge_case(self):
        self.assertFalse(dif_Square(4))

    def test_edge_case2(self):
        self.assertFalse(dif_Square(8))

    def test_edge_case3(self):
        self.assertTrue(dif_Square(12))

    def test_edge_case4(self):
        self.assertFalse(dif_Square(0))

    def test_edge_case5(self):
        self.assertFalse(dif_Square(3))

    def test_edge_case6(self):
        self.assertFalse(dif_Square(7))

    def test_edge_case7(self):
        self.assertFalse(dif_Square(1))

    def test_edge_case8(self):
        self.assertFalse(dif_Square(5))

    def test_edge_case9(self):
        self.assertFalse(dif_Square(9))

    def test_edge_case10(self):
        self.assertFalse(dif_Square(11))
