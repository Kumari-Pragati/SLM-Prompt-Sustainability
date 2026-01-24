import unittest
from mbpp_348_code import find_ways

class TestFindWays(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_ways(4), 1)

    def test_edge_case(self):
        self.assertEqual(find_ways(5), 1)

    def test_edge_case2(self):
        self.assertEqual(find_ways(6), 2)

    def test_edge_case3(self):
        self.assertEqual(find_ways(7), 2)

    def test_edge_case4(self):
        self.assertEqual(find_ways(8), 3)

    def test_edge_case5(self):
        self.assertEqual(find_ways(9), 3)

    def test_edge_case6(self):
        self.assertEqual(find_ways(10), 5)

    def test_edge_case7(self):
        self.assertEqual(find_ways(11), 5)

    def test_edge_case8(self):
        self.assertEqual(find_ways(12), 7)

    def test_edge_case9(self):
        self.assertEqual(find_ways(13), 7)

    def test_edge_case10(self):
        self.assertEqual(find_ways(14), 9)

    def test_edge_case11(self):
        self.assertEqual(find_ways(15), 9)

    def test_edge_case12(self):
        self.assertEqual(find_ways(16), 12)

    def test_edge_case13(self):
        self.assertEqual(find_ways(17), 12)

    def test_edge_case14(self):
        self.assertEqual(find_ways(18), 15)

    def test_edge_case15(self):
        self.assertEqual(find_ways(19), 15)

    def test_edge_case16(self):
        self.assertEqual(find_ways(20), 18)

    def test_edge_case17(self):
        self.assertEqual(find_ways(21), 18)

    def test_edge_case18(self):
        self.assertEqual(find_ways(22), 20)

    def test_edge_case19(self):
        self.assertEqual(find_ways(23), 20)

    def test_edge_case20(self):
        self.assertEqual(find_ways(24), 22)

    def test_edge_case21(self):
        self.assertEqual(find_ways(25), 22)

    def test_edge_case22(self):
        self.assertEqual(find_ways(26), 24)

    def test_edge_case23(self):
        self.assertEqual(find_ways(27), 24)

    def test_edge_case24(self):
        self.assertEqual(find_ways(28), 25)

    def test_edge_case25(self):
        self.assertEqual(find_ways(29), 25)

    def test_edge_case26(self):
        self.assertEqual(find_ways(30), 26)

    def test_edge_case27(self):
        self.assertEqual(find_ways(31), 26)

    def test_edge_case28(self):
        self.assertEqual(find_ways(32), 27)

    def test_edge_case29(self):
        self.assertEqual(find_ways(33), 27)

    def test_edge_case30(self):
        self.assertEqual(find_ways(34), 28)

    def test_edge_case31(self):
        self.assertEqual(find_ways(35), 28)

    def test_edge_case32(self):
        self.assertEqual(find_ways(36), 29)

    def test_edge_case33(self):
        self.assertEqual(find_ways(37), 29)

    def test_edge_case34(self):
        self.assertEqual(find_ways(38), 30)

    def test_edge_case35(self):
        self.assertEqual(find_ways(39), 30)

    def test_edge_case36(self):
        self.assertEqual(find_ways(40), 31)

    def test_edge_case37(self):
        self.assertEqual(find_ways(41), 31)

    def test_edge_case38(self):
        self.assertEqual(find_ways(42), 32)

    def test_edge_case39(self):
        self.assertEqual(find_ways(43), 32)

    def test_edge_case40(self):
        self.assertEqual(find_ways(44), 33)

    def test_edge_case41(self):
        self.assertEqual(find_ways(45), 33)

    def test_edge_case42(self):
        self.assertEqual(find_ways(46), 34)

    def test_edge_case43(self):
        self.assertEqual(find_ways(47), 34)

    def test_edge_case44(self):
        self.assertEqual(find_ways(48), 35)

    def test_edge_case45(self):
        self.assertEqual(find_ways(49), 35)

    def test_edge_case46(self):
        self.assertEqual(find_ways(50), 36)

    def test_edge_case47(self):
        self.assertEqual(find_ways(51), 36)

    def test_edge_case48(self):
        self.assertEqual(find_ways(52), 37)

    def test_edge_case49(self):
        self.assertEqual(find_ways(53), 37)

    def test_edge_case