import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_not_prime(4))

    def test_edge_case(self):
        self.assertTrue(is_not_prime(1))

    def test_edge_case2(self):
        self.assertFalse(is_not_prime(2))

    def test_edge_case3(self):
        self.assertFalse(is_not_prime(3))

    def test_edge_case4(self):
        self.assertFalse(is_not_prime(5))

    def test_edge_case5(self):
        self.assertFalse(is_not_prime(7))

    def test_edge_case6(self):
        self.assertFalse(is_not_prime(11))

    def test_edge_case7(self):
        self.assertFalse(is_not_prime(13))

    def test_edge_case8(self):
        self.assertFalse(is_not_prime(17))

    def test_edge_case9(self):
        self.assertFalse(is_not_prime(19))

    def test_edge_case10(self):
        self.assertFalse(is_not_prime(23))

    def test_edge_case11(self):
        self.assertFalse(is_not_prime(29))

    def test_edge_case12(self):
        self.assertFalse(is_not_prime(31))

    def test_edge_case13(self):
        self.assertFalse(is_not_prime(37))

    def test_edge_case14(self):
        self.assertFalse(is_not_prime(41))

    def test_edge_case15(self):
        self.assertFalse(is_not_prime(43))

    def test_edge_case16(self):
        self.assertFalse(is_not_prime(47))

    def test_edge_case17(self):
        self.assertFalse(is_not_prime(53))

    def test_edge_case18(self):
        self.assertFalse(is_not_prime(59))

    def test_edge_case19(self):
        self.assertFalse(is_not_prime(61))

    def test_edge_case20(self):
        self.assertFalse(is_not_prime(67))

    def test_edge_case21(self):
        self.assertFalse(is_not_prime(71))

    def test_edge_case22(self):
        self.assertFalse(is_not_prime(73))

    def test_edge_case23(self):
        self.assertFalse(is_not_prime(79))

    def test_edge_case24(self):
        self.assertFalse(is_not_prime(83))

    def test_edge_case25(self):
        self.assertFalse(is_not_prime(89))

    def test_edge_case26(self):
        self.assertFalse(is_not_prime(97))

    def test_edge_case27(self):
        self.assertFalse(is_not_prime(101))

    def test_edge_case28(self):
        self.assertFalse(is_not_prime(103))

    def test_edge_case29(self):
        self.assertFalse(is_not_prime(107))

    def test_edge_case30(self):
        self.assertFalse(is_not_prime(109))

    def test_edge_case31(self):
        self.assertFalse(is_not_prime(113))

    def test_edge_case32(self):
        self.assertFalse(is_not_prime(127))

    def test_edge_case33(self):
        self.assertFalse(is_not_prime(131))

    def test_edge_case34(self):
        self.assertFalse(is_not_prime(137))

    def test_edge_case35(self):
        self.assertFalse(is_not_prime(139))

    def test_edge_case36(self):
        self.assertFalse(is_not_prime(149))

    def test_edge_case37(self):
        self.assertFalse(is_not_prime(151))

    def test_edge_case38(self):
        self.assertFalse(is_not_prime(157))

    def test_edge_case39(self):
        self.assertFalse(is_not_prime(163))

    def test_edge_case40(self):
        self.assertFalse(is_not_prime(167))

    def test_edge_case41(self):
        self.assertFalse(is_not_prime(173))

    def test_edge_case42(self):
        self.assertFalse(is_not_prime(179))

    def test_edge_case43(self):
        self.assertFalse(is_not_prime(181))

    def test_edge_case44(self):
        self.assertFalse(is_not_prime(191))

    def test_edge_case45(self):
        self.assertFalse(is_not_prime(193))

    def test_edge_case46(self):
        self.assertFalse(is_not_prime(197))

    def test_edge_case47(self):
        self.assertFalse(is_not_prime(199))

    def test_edge_case48(self):
        self.assertFalse(is_not_prime(211))

    def test_edge_case49(self):
        self.assertFalse(is_not_prime(221))

    def test_edge_case50(self):
        self.assertFalse(is_not_prime(223))

    def test_edge_case51(self):
        self.assertFalse(is_not_prime(227))

    def test_edge_case52(self):
        self.assertFalse(is_not_prime(229))

    def test_edge_case53(self):
        self.assertFalse(is_not_prime(233))

    def test_edge_case54(self):
        self.assertFalse(is_not_prime(239))

    def test_edge_case55(self):
        self.assertFalse(is_not_prime(241))

    def test_edge_case56(self):
        self.assertFalse(is_not_prime(251))

    def test_edge_case57(self):
        self.assertFalse(is_not_prime(257))

    def test_edge_case58(self):
        self.assertFalse(is_not_prime(263))