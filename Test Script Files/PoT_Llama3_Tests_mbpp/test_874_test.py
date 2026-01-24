import unittest
from mbpp_874_code import check_Concat

class TestCheckConcat(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Concat("abc", "ab"))

    def test_edge_case1(self):
        self.assertFalse(check_Concat("abc", "a"))

    def test_edge_case2(self):
        self.assertTrue(check_Concat("abc", "abc"))

    def test_edge_case3(self):
        self.assertFalse(check_Concat("abc", "abcd"))

    def test_edge_case4(self):
        self.assertTrue(check_Concat("abc", "b"))

    def test_edge_case5(self):
        self.assertFalse(check_Concat("abc", ""))

    def test_edge_case6(self):
        self.assertTrue(check_Concat("abc", "c"))

    def test_edge_case7(self):
        self.assertFalse(check_Concat("abc", "d"))

    def test_edge_case8(self):
        self.assertTrue(check_Concat("abc", "a"))

    def test_edge_case9(self):
        self.assertFalse(check_Concat("abc", "b"))

    def test_edge_case10(self):
        self.assertTrue(check_Concat("abc", "c"))

    def test_edge_case11(self):
        self.assertFalse(check_Concat("abc", "d"))

    def test_edge_case12(self):
        self.assertTrue(check_Concat("abc", "e"))

    def test_edge_case13(self):
        self.assertFalse(check_Concat("abc", "f"))

    def test_edge_case14(self):
        self.assertTrue(check_Concat("abc", "g"))

    def test_edge_case15(self):
        self.assertFalse(check_Concat("abc", "h"))

    def test_edge_case16(self):
        self.assertTrue(check_Concat("abc", "i"))

    def test_edge_case17(self):
        self.assertFalse(check_Concat("abc", "j"))

    def test_edge_case18(self):
        self.assertTrue(check_Concat("abc", "k"))

    def test_edge_case19(self):
        self.assertFalse(check_Concat("abc", "l"))

    def test_edge_case20(self):
        self.assertTrue(check_Concat("abc", "m"))

    def test_edge_case21(self):
        self.assertFalse(check_Concat("abc", "n"))

    def test_edge_case22(self):
        self.assertTrue(check_Concat("abc", "o"))

    def test_edge_case23(self):
        self.assertFalse(check_Concat("abc", "p"))

    def test_edge_case24(self):
        self.assertTrue(check_Concat("abc", "q"))

    def test_edge_case25(self):
        self.assertFalse(check_Concat("abc", "r"))

    def test_edge_case26(self):
        self.assertTrue(check_Concat("abc", "s"))

    def test_edge_case27(self):
        self.assertFalse(check_Concat("abc", "t"))

    def test_edge_case28(self):
        self.assertTrue(check_Concat("abc", "u"))

    def test_edge_case29(self):
        self.assertFalse(check_Concat("abc", "v"))

    def test_edge_case30(self):
        self.assertTrue(check_Concat("abc", "w"))

    def test_edge_case31(self):
        self.assertFalse(check_Concat("abc", "x"))

    def test_edge_case32(self):
        self.assertTrue(check_Concat("abc", "y"))

    def test_edge_case33(self):
        self.assertFalse(check_Concat("abc", "z"))

    def test_edge_case34(self):
        self.assertTrue(check_Concat("abc", "a"))

    def test_edge_case35(self):
        self.assertFalse(check_Concat("abc", "b"))

    def test_edge_case36(self):
        self.assertTrue(check_Concat("abc", "c"))

    def test_edge_case37(self):
        self.assertFalse(check_Concat("abc", "d"))

    def test_edge_case38(self):
        self.assertTrue(check_Concat("abc", "e"))

    def test_edge_case39(self):
        self.assertFalse(check_Concat("abc", "f"))

    def test_edge_case40(self):
        self.assertTrue(check_Concat("abc", "g"))

    def test_edge_case41(self):
        self.assertFalse(check_Concat("abc", "h"))

    def test_edge_case42(self):
        self.assertTrue(check_Concat("abc", "i"))

    def test_edge_case43(self):
        self.assertFalse(check_Concat("abc", "j"))

    def test_edge_case44(self):
        self.assertTrue(check_Concat("abc", "k"))

    def test_edge_case45(self):
        self.assertFalse(check_Concat("abc", "l"))

    def test_edge_case46(self):
        self.assertTrue(check_Concat("abc", "m"))

    def test_edge_case47(self):
        self.assertFalse(check_Concat("abc", "n"))

    def test_edge_case48(self):
        self.assertTrue(check_Concat("abc", "o"))

    def test_edge_case49(self):
        self.assertFalse(check_Concat("abc", "p"))

    def test_edge_case50