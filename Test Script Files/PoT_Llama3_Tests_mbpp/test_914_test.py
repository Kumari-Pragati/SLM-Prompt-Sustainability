import unittest
from mbpp_914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Two_Alter("abcde"))

    def test_edge_case1(self):
        self.assertFalse(is_Two_Alter("aabbcc"))

    def test_edge_case2(self):
        self.assertTrue(is_Two_Alter("abcdef"))

    def test_edge_case3(self):
        self.assertFalse(is_Two_Alter("aaabbb"))

    def test_edge_case4(self):
        self.assertTrue(is_Two_Alter("abcdefg"))

    def test_edge_case5(self):
        self.assertFalse(is_Two_Alter("aabbccdd"))

    def test_edge_case6(self):
        self.assertTrue(is_Two_Alter("abcdefgh"))

    def test_edge_case7(self):
        self.assertFalse(is_Two_Alter("aabbccddff"))

    def test_edge_case8(self):
        self.assertTrue(is_Two_Alter("abcdefghij"))

    def test_edge_case9(self):
        self.assertFalse(is_Two_Alter("aabbccddffgg"))

    def test_edge_case10(self):
        self.assertTrue(is_Two_Alter("abcdefghijkl"))

    def test_edge_case11(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghh"))

    def test_edge_case12(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmn"))

    def test_edge_case13(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhi"))

    def test_edge_case14(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnop"))

    def test_edge_case15(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhii"))

    def test_edge_case16(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqr"))

    def test_edge_case17(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiij"))

    def test_edge_case18(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrt"))

    def test_edge_case19(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijk"))

    def test_edge_case20(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstu"))

    def test_edge_case21(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijkl"))

    def test_edge_case22(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuv"))

    def test_edge_case23(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijkll"))

    def test_edge_case24(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvw"))

    def test_edge_case25(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijklmn"))

    def test_edge_case26(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvwx"))

    def test_edge_case27(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijkllmn"))

    def test_edge_case28(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvwxy"))

    def test_edge_case29(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijklmnop"))

    def test_edge_case30(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvwxyz"))

    def test_edge_case31(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijkllmnop"))

    def test_edge_case32(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvwxyza"))

    def test_edge_case33(self):
        self.assertFalse(is_Two_Alter("aabbccddffgghhiijklmnopqr"))

    def test_edge_case34(self):
        self.assertTrue(is_Two_Alter("abcdefghijklmnopqrstuvwxyzab"))

    def test_edge_case35(self):