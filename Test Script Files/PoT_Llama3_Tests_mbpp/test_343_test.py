import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(dig_let("hello123"), (4, 3))

    def test_edge1(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_edge2(self):
        self.assertEqual(dig_let("123"), (0, 3))

    def test_edge3(self):
        self.assertEqual(dig_let("abc"), (3, 0))

    def test_edge4(self):
        self.assertEqual(dig_let("a1b2c3"), (3, 3))

    def test_edge5(self):
        self.assertEqual(dig_let("123abc"), (3, 3))

    def test_edge6(self):
        self.assertEqual(dig_let("abc123"), (3, 3))

    def test_edge7(self):
        self.assertEqual(dig_let("a1b2c3d4e5"), (5, 5))

    def test_edge8(self):
        self.assertEqual(dig_let("123abc456"), (6, 6))

    def test_edge9(self):
        self.assertEqual(dig_let("a1b2c3d4e5f6g7h8i9j10"), (10, 10))

    def test_edge10(self):
        self.assertEqual(dig_let("a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q17r18s19t20"), (20, 20))
