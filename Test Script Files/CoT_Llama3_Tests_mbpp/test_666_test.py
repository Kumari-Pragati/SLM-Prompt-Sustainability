import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char("hello", 'o'), 1)

    def test_edge_case(self):
        self.assertEqual(count_char("hello", 'x'), 0)

    def test_edge_case2(self):
        self.assertEqual(count_char("", 'a'), 0)

    def test_edge_case3(self):
        self.assertEqual(count_char("a", 'a'), 1)

    def test_edge_case4(self):
        self.assertEqual(count_char("a", 'b'), 0)

    def test_edge_case5(self):
        self.assertEqual(count_char("abc", 'c'), 1)

    def test_edge_case6(self):
        self.assertEqual(count_char("abc", 'd'), 0)

    def test_edge_case7(self):
        self.assertEqual(count_char("abc", 'a'), 1)

    def test_edge_case8(self):
        self.assertEqual(count_char("abc", 'b'), 1)

    def test_edge_case9(self):
        self.assertEqual(count_char("abc", 'c'), 1)

    def test_edge_case10(self):
        self.assertEqual(count_char("abc", 'd'), 1)

    def test_edge_case11(self):
        self.assertEqual(count_char("abc", 'e'), 0)

    def test_edge_case12(self):
        self.assertEqual(count_char("abc", 'f'), 0)

    def test_edge_case13(self):
        self.assertEqual(count_char("abc", 'g'), 0)

    def test_edge_case14(self):
        self.assertEqual(count_char("abc", 'h'), 0)

    def test_edge_case15(self):
        self.assertEqual(count_char("abc", 'i'), 0)

    def test_edge_case16(self):
        self.assertEqual(count_char("abc", 'j'), 0)

    def test_edge_case17(self):
        self.assertEqual(count_char("abc", 'k'), 0)

    def test_edge_case18(self):
        self.assertEqual(count_char("abc", 'l'), 0)

    def test_edge_case19(self):
        self.assertEqual(count_char("abc",'m'), 0)

    def test_edge_case20(self):
        self.assertEqual(count_char("abc", 'n'), 0)

    def test_edge_case21(self):
        self.assertEqual(count_char("abc", 'o'), 1)

    def test_edge_case22(self):
        self.assertEqual(count_char("abc", 'p'), 0)

    def test_edge_case23(self):
        self.assertEqual(count_char("abc", 'q'), 0)

    def test_edge_case24(self):
        self.assertEqual(count_char("abc", 'r'), 0)

    def test_edge_case25(self):
        self.assertEqual(count_char("abc",'s'), 0)

    def test_edge_case26(self):
        self.assertEqual(count_char("abc", 't'), 0)

    def test_edge_case27(self):
        self.assertEqual(count_char("abc", 'u'), 0)

    def test_edge_case28(self):
        self.assertEqual(count_char("abc", 'v'), 0)

    def test_edge_case29(self):
        self.assertEqual(count_char("abc", 'w'), 0)

    def test_edge_case30(self):
        self.assertEqual(count_char("abc", 'x'), 0)

    def test_edge_case31(self):
        self.assertEqual(count_char("abc", 'y'), 0)

    def test_edge_case32(self):
        self.assertEqual(count_char("abc", 'z'), 0)

    def test_edge_case33(self):
        self.assertEqual(count_char("abc", 'a'), 1)

    def test_edge_case34(self):
        self.assertEqual(count_char("abc", 'b'), 1)

    def test_edge_case35(self):
        self.assertEqual(count_char("abc", 'c'), 1)

    def test_edge_case36(self):
        self.assertEqual(count_char("abc", 'd'), 1)

    def test_edge_case37(self):
        self.assertEqual(count_char("abc", 'e'), 1)

    def test_edge_case38(self):
        self.assertEqual(count_char("abc", 'f'), 1)

    def test_edge_case39(self):
        self.assertEqual(count_char("abc", 'g'), 1)

    def test_edge_case40(self):
        self.assertEqual(count_char("abc", 'h'), 1)

    def test_edge_case41(self):
        self.assertEqual(count_char("abc", 'i'), 1)

    def test_edge_case42(self):
        self.assertEqual(count_char("abc", 'j'), 1)

    def test_edge_case43(self):
        self.assertEqual(count_char("abc", 'k'), 1)

    def test_edge_case44(self):
        self.assertEqual(count_char("abc", 'l'), 1)

    def test_edge_case45(self):
        self.assertEqual(count_char("abc",'m'),