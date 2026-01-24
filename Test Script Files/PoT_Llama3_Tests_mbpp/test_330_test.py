import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_char("Hello world, this is a test"), ["Hello", "world", "this", "test"])

    def test_edge1(self):
        self.assertEqual(find_char(""), [])

    def test_edge2(self):
        self.assertEqual(find_char("a"), [])

    def test_edge3(self):
        self.assertEqual(find_char("abc"), [])

    def test_edge4(self):
        self.assertEqual(find_char("abcde"), ["abc", "abcde"])

    def test_edge5(self):
        self.assertEqual(find_char("abcdef"), ["abcdef"])

    def test_edge6(self):
        self.assertEqual(find_char("abcdefg"), ["abcdefg"])

    def test_edge7(self):
        self.assertEqual(find_char("abcdefgh"), ["abcdefgh"])

    def test_edge8(self):
        self.assertEqual(find_char("abcdefghi"), ["abcdefghi"])

    def test_edge9(self):
        self.assertEqual(find_char("abcdefhij"), ["abcdefhij"])

    def test_edge10(self):
        self.assertEqual(find_char("abcdefhijk"), ["abcdefhijk"])

    def test_edge11(self):
        self.assertEqual(find_char("abcdefhijkl"), ["abcdefhijkl"])

    def test_edge12(self):
        self.assertEqual(find_char("abcdefhijklm"), ["abcdefhijklm"])

    def test_edge13(self):
        self.assertEqual(find_char("abcdefhijklmn"), ["abcdefhijklmn"])

    def test_edge14(self):
        self.assertEqual(find_char("abcdefhijklmno"), ["abcdefhijklmno"])

    def test_edge15(self):
        self.assertEqual(find_char("abcdefhijklmnop"), ["abcdefhijklmnop"])

    def test_edge16(self):
        self.assertEqual(find_char("abcdefhijklmnopq"), ["abcdefhijklmnopq"])

    def test_edge17(self):
        self.assertEqual(find_char("abcdefhijklmnopr"), ["abcdefhijklmnopr"])

    def test_edge18(self):
        self.assertEqual(find_char("abcdefhijklmnopqr"), ["abcdefhijklmnopqr"])

    def test_edge19(self):
        self.assertEqual(find_char("abcdefhijklmnopqrs"), ["abcdefhijklmnopqrs"])

    def test_edge20(self):
        self.assertEqual(find_char("abcdefhijklmnopqrst"), ["abcdefhijklmnopqrst"])

    def test_edge21(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstu"), ["abcdefhijklmnopqrstu"])

    def test_edge22(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuv"), ["abcdefhijklmnopqrstuv"])

    def test_edge23(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuva"), ["abcdefhijklmnopqrstuva"])

    def test_edge24(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvab"), ["abcdefhijklmnopqrstuvab"])

    def test_edge25(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvaab"), ["abcdefhijklmnopqrstuvaab"])

    def test_edge26(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvabc"), ["abcdefhijklmnopqrstuvabc"])

    def test_edge27(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvaabc"), ["abcdefhijklmnopqrstuvaabc"])

    def test_edge28(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvabcd"), ["abcdefhijklmnopqrstuvabcd"])

    def test_edge29(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvaabcde"), ["abcdefhijklmnopqrstuvaabcde"])

    def test_edge30(self):
        self.assertEqual(find_char("abcdefhijklmnopqrstuvabcdef"), ["abcdefhijklmnopqrstuvabcdef"])
