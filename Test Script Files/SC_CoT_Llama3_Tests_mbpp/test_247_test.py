import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(lps("abab"), 4)

    def test_edge1(self):
        self.assertEqual(lps(""), 0)

    def test_edge2(self):
        self.assertEqual(lps("a"), 1)

    def test_edge3(self):
        self.assertEqual(lps("aa"), 2)

    def test_edge4(self):
        self.assertEqual(lps("aba"), 3)

    def test_edge5(self):
        self.assertEqual(lps("ababab"), 6)

    def test_edge6(self):
        self.assertEqual(lps("abc"), 1)

    def test_edge7(self):
        self.assertEqual(lps("abcd"), 1)

    def test_edge8(self):
        self.assertEqual(lps("abcde"), 1)

    def test_edge9(self):
        self.assertEqual(lps("abcdef"), 1)

    def test_edge10(self):
        self.assertEqual(lps("abcdefg"), 1)

    def test_edge11(self):
        self.assertEqual(lps("abcdefgh"), 1)

    def test_edge12(self):
        self.assertEqual(lps("abcdefghi"), 1)

    def test_edge13(self):
        self.assertEqual(lps("abcdefghij"), 1)

    def test_edge14(self):
        self.assertEqual(lps("abcdefghijk"), 1)

    def test_edge15(self):
        self.assertEqual(lps("abcdefghijkl"), 1)

    def test_edge16(self):
        self.assertEqual(lps("abcdefghijkla"), 1)

    def test_edge17(self):
        self.assertEqual(lps("abcdefghijklab"), 1)

    def test_edge18(self):
        self.assertEqual(lps("abcdefghijklabc"), 1)

    def test_edge19(self):
        self.assertEqual(lps("abcdefghijklabcd"), 1)

    def test_edge20(self):
        self.assertEqual(lps("abcdefghijklabcde"), 1)

    def test_edge21(self):
        self.assertEqual(lps("abcdefghijklabcdef"), 1)

    def test_edge22(self):
        self.assertEqual(lps("abcdefghijklabcdefg"), 1)

    def test_edge23(self):
        self.assertEqual(lps("abcdefghijklabcdefgh"), 1)

    def test_edge24(self):
        self.assertEqual(lps("abcdefghijklabcdefghi"), 1)

    def test_edge25(self):
        self.assertEqual(lps("abcdefghijklabcdefghij"), 1)

    def test_edge26(self):
        self.assertEqual(lps("abcdefghijklabcdefghijk"), 1)

    def test_edge27(self):
        self.assertEqual(lps("abcdefghijklabcdefghijkl"), 1)

    def test_edge28(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklm"), 1)

    def test_edge29(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmn"), 1)

    def test_edge30(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmno"), 1)

    def test_edge31(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnop"), 1)

    def test_edge32(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopq"), 1)

    def test_edge33(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqr"), 1)

    def test_edge34(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrs"), 1)

    def test_edge35(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrst"), 1)

    def test_edge36(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstu"), 1)

    def test_edge37(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuv"), 1)

    def test_edge38(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwx"), 1)

    def test_edge39(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwxxy"), 1)

    def test_edge40(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwxxyyz"), 1)

    def test_edge41(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwxxyyzza"), 1)

    def test_edge42(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwxxyyzzzb"), 1)

    def test_edge43(self):
        self.assertEqual(lps("abcdefghijklabcdefghijklmnopqrstuwxxyyzzzbc"), 1)

    def