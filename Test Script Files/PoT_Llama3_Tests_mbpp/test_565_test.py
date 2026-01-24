import unittest
from mbpp_565_code import split

class TestSplit(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(split('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_edge(self):
        self.assertEqual(split(''), [])

    def test_edge2(self):
        self.assertEqual(split('a'), ['a'])

    def test_edge3(self):
        self.assertEqual(split('abc'), ['a', 'b', 'c'])

    def test_edge4(self):
        self.assertEqual(split('abcde'), ['a', 'b', 'c', 'd', 'e'])

    def test_edge5(self):
        self.assertEqual(split('abcdefg'), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_edge6(self):
        self.assertEqual(split('abcdefgh'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_edge7(self):
        self.assertEqual(split('abcdefghi'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    def test_edge8(self):
        self.assertEqual(split('abcdefghij'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

    def test_edge9(self):
        self.assertEqual(split('abcdefghijk'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])

    def test_edge10(self):
        self.assertEqual(split('abcdefghijklm'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m'])

    def test_edge11(self):
        self.assertEqual(split('abcdefghijklmn'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'])

    def test_edge12(self):
        self.assertEqual(split('abcdefghijklmno'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o'])

    def test_edge13(self):
        self.assertEqual(split('abcdefghijklmnop'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p'])

    def test_edge14(self):
        self.assertEqual(split('abcdefghijklmnopq'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q'])

    def test_edge15(self):
        self.assertEqual(split('abcdefghijklmnopqr'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r'])

    def test_edge16(self):
        self.assertEqual(split('abcdefghijklmnopqrt'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 't'])

    def test_edge17(self):
        self.assertEqual(split('abcdefghijklmnopqrts'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 't','s'])

    def test_edge18(self):
        self.assertEqual(split('abcdefghijklmnopqrst'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 't','s', 'u'])

    def test_edge19(self):
        self.assertEqual(split('abcdefghijklmnopqrstu'), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 't','s