import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Two_Alter('abcde'))

    def test_edge_case1(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case2(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case3(self):
        self.assertFalse(is_Two_Alter('abcdef'))

    def test_edge_case4(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case5(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case6(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case7(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case8(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case9(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case10(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case11(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case12(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case13(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case14(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case15(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case16(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case17(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case18(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case19(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case20(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case21(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case22(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case23(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case24(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case25(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case26(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case27(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case28(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case29(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case30(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case31(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case32(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case33(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case34(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case35(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case36(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case37(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case38(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case39(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case40(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case41(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case42(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case43(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case44(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case45(self):
        self.assertFalse(is_Two_Alter('a'))

    def test_edge_case46(self):
        self.assertFalse(is_Two_Alter(''))

    def test_edge_case47(self):
        self.assertFalse(is_Two_Alter('aabb'))

    def test_edge_case48(self):
        self.assertTrue(is_Two_Alter('abab'))

    def test_edge_case49(self):
        self.assertFalse(is_Two_Alter('abc'))

    def test_edge_case50(self):
        self.assertTrue(is_Two_Alter('abcabc'))

    def test_edge_case51(self):
        self.assertFalse(is_Two_Alter('aabbcc'))

    def test_edge_case52(self):
        self.assertTrue(is_Two_Alter('ababab'))

    def test_edge_case53(self