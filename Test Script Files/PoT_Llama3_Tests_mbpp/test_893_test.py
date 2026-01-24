import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6]]), [[3], [6]])

    def test_edge1(self):
        self.assertEqual(Extract([[]]), [[]])

    def test_edge2(self):
        self.assertEqual(Extract([['a']]), [['a']])

    def test_edge3(self):
        self.assertEqual(Extract([['a', 'b', 'c']]), [['c']])

    def test_edge4(self):
        self.assertEqual(Extract([['a', 'b']]), [['b']])

    def test_edge5(self):
        self.assertEqual(Extract([['a']]), [['a']])

    def test_edge6(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd']]), [['d']])

    def test_edge7(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e']]), [['e']])

    def test_edge8(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f']]), [['f']])

    def test_edge9(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g']]), [['g']])

    def test_edge10(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]), [['h']])

    def test_edge11(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]), [['i']])

    def test_edge12(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']]), [['j']])

    def test_edge13(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']]), [['k']])

    def test_edge14(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']]), [['l']])

    def test_edge15(self):
        self.assertEqual(Extract([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m']]), [['m']])
