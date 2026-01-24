import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_num(10, 2), 10)

    def test_edge_case(self):
        self.assertEqual(round_num(11, 2), 10)

    def test_edge_case2(self):
        self.assertEqual(round_num(12, 2), 12)

    def test_edge_case3(self):
        self.assertEqual(round_num(10, 1), 10)

    def test_edge_case4(self):
        self.assertEqual(round_num(10, 3), 10)

    def test_edge_case5(self):
        self.assertEqual(round_num(11, 3), 12)

    def test_edge_case6(self):
        self.assertEqual(round_num(12, 3), 12)

    def test_edge_case7(self):
        self.assertEqual(round_num(10, 4), 8)

    def test_edge_case8(self):
        self.assertEqual(round_num(11, 4), 12)

    def test_edge_case9(self):
        self.assertEqual(round_num(12, 4), 12)

    def test_edge_case10(self):
        self.assertEqual(round_num(10, 5), 10)

    def test_edge_case11(self):
        self.assertEqual(round_num(11, 5), 10)

    def test_edge_case12(self):
        self.assertEqual(round_num(12, 5), 12)

    def test_edge_case13(self):
        self.assertEqual(round_num(10, 6), 10)

    def test_edge_case14(self):
        self.assertEqual(round_num(11, 6), 12)

    def test_edge_case15(self):
        self.assertEqual(round_num(12, 6), 12)

    def test_edge_case16(self):
        self.assertEqual(round_num(10, 7), 10)

    def test_edge_case17(self):
        self.assertEqual(round_num(11, 7), 12)

    def test_edge_case18(self):
        self.assertEqual(round_num(12, 7), 12)

    def test_edge_case19(self):
        self.assertEqual(round_num(10, 8), 8)

    def test_edge_case20(self):
        self.assertEqual(round_num(11, 8), 12)

    def test_edge_case21(self):
        self.assertEqual(round_num(12, 8), 12)

    def test_edge_case22(self):
        self.assertEqual(round_num(10, 9), 10)

    def test_edge_case23(self):
        self.assertEqual(round_num(11, 9), 12)

    def test_edge_case24(self):
        self.assertEqual(round_num(12, 9), 12)

    def test_edge_case25(self):
        self.assertEqual(round_num(10, 10), 10)

    def test_edge_case26(self):
        self.assertEqual(round_num(11, 10), 10)

    def test_edge_case27(self):
        self.assertEqual(round_num(12, 10), 12)

    def test_edge_case28(self):
        self.assertEqual(round_num(10, 11), 10)

    def test_edge_case29(self):
        self.assertEqual(round_num(11, 11), 10)

    def test_edge_case30(self):
        self.assertEqual(round_num(12, 11), 12)

    def test_edge_case31(self):
        self.assertEqual(round_num(10, 12), 10)

    def test_edge_case32(self):
        self.assertEqual(round_num(11, 12), 12)

    def test_edge_case33(self):
        self.assertEqual(round_num(12, 12), 12)

    def test_edge_case34(self):
        self.assertEqual(round_num(10, 13), 10)

    def test_edge_case35(self):
        self.assertEqual(round_num(11, 13), 12)

    def test_edge_case36(self):
        self.assertEqual(round_num(12, 13), 12)

    def test_edge_case37(self):
        self.assertEqual(round_num(10, 14), 10)

    def test_edge_case38(self):
        self.assertEqual(round_num(11, 14), 12)

    def test_edge_case39(self):
        self.assertEqual(round_num(12, 14), 12)

    def test_edge_case40(self):
        self.assertEqual(round_num(10, 15), 10)

    def test_edge_case41(self):
        self.assertEqual(round_num(11, 15), 12)

    def test_edge_case42(self):
        self.assertEqual(round_num(12, 15), 12)

    def test_edge_case43(self):
        self.assertEqual(round_num(10, 16), 10)

    def test_edge_case44(self):
        self.assertEqual(round_num(11, 16), 12)

    def test_edge_case45(self):
        self.assertEqual(round_num(12,