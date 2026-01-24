import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Convert("Hello World"), ['Hello', 'World'])

    def test_edge1(self):
        self.assertEqual(Convert(""), [])

    def test_edge2(self):
        self.assertEqual(Convert("   "), [])

    def test_edge3(self):
        self.assertEqual(Convert("a"), ['a'])

    def test_edge4(self):
        self.assertEqual(Convert("a b c"), ['a', 'b', 'c'])

    def test_edge5(self):
        self.assertEqual(Convert("a b c d"), ['a', 'b', 'c', 'd'])

    def test_edge6(self):
        self.assertEqual(Convert("a b c d e"), ['a', 'b', 'c', 'd', 'e'])

    def test_edge7(self):
        self.assertEqual(Convert("a b c d e f"), ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_edge8(self):
        self.assertEqual(Convert("a b c d e f g"), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_edge9(self):
        self.assertEqual(Convert("a b c d e f g h"), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_edge10(self):
        self.assertEqual(Convert("a b c d e f g h i"), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
