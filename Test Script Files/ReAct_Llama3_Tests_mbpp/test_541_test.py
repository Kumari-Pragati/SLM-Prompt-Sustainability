import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_abundant(self):
        self.assertTrue(check_abundant(12))

    def test_not_abundant(self):
        self.assertFalse(check_abundant(5))

    def test_edge_case(self):
        self.assertTrue(check_abundant(24))

    def test_edge_case2(self):
        self.assertFalse(check_abundant(7))

    def test_edge_case3(self):
        self.assertTrue(check_abundant(36))

    def test_edge_case4(self):
        self.assertFalse(check_abundant(11))

    def test_edge_case5(self):
        self.assertTrue(check_abundant(48))

    def test_edge_case6(self):
        self.assertFalse(check_abundant(13))

    def test_edge_case7(self):
        self.assertTrue(check_abundant(60))

    def test_edge_case8(self):
        self.assertFalse(check_abundant(15))

    def test_edge_case9(self):
        self.assertTrue(check_abundant(72))

    def test_edge_case10(self):
        self.assertFalse(check_abundant(17))

    def test_edge_case11(self):
        self.assertTrue(check_abundant(96))

    def test_edge_case12(self):
        self.assertFalse(check_abundant(19))

    def test_edge_case13(self):
        self.assertTrue(check_abundant(120))

    def test_edge_case14(self):
        self.assertFalse(check_abundant(21))

    def test_edge_case15(self):
        self.assertTrue(check_abundant(144))

    def test_edge_case16(self):
        self.assertFalse(check_abundant(23))

    def test_edge_case17(self):
        self.assertTrue(check_abundant(168))

    def test_edge_case18(self):
        self.assertFalse(check_abundant(25))

    def test_edge_case19(self):
        self.assertTrue(check_abundant(192))

    def test_edge_case20(self):
        self.assertFalse(check_abundant(27))

    def test_edge_case21(self):
        self.assertTrue(check_abundant(216))

    def test_edge_case22(self):
        self.assertFalse(check_abundant(29))

    def test_edge_case23(self):
        self.assertTrue(check_abundant(240))

    def test_edge_case24(self):
        self.assertFalse(check_abundant(31))

    def test_edge_case25(self):
        self.assertTrue(check_abundant(264))

    def test_edge_case26(self):
        self.assertFalse(check_abundant(33))

    def test_edge_case27(self):
        self.assertTrue(check_abundant(288))

    def test_edge_case28(self):
        self.assertFalse(check_abundant(35))

    def test_edge_case29(self):
        self.assertTrue(check_abundant(312))

    def test_edge_case30(self):
        self.assertFalse(check_abundant(37))

    def test_edge_case31(self):
        self.assertTrue(check_abundant(336))

    def test_edge_case32(self):
        self.assertFalse(check_abundant(39))

    def test_edge_case33(self):
        self.assertTrue(check_abundant(360))

    def test_edge_case34(self):
        self.assertFalse(check_abundant(41))

    def test_edge_case35(self):
        self.assertTrue(check_abundant(384))

    def test_edge_case36(self):
        self.assertFalse(check_abundant(43))

    def test_edge_case37(self):
        self.assertTrue(check_abundant(408))

    def test_edge_case38(self):
        self.assertFalse(check_abundant(45))

    def test_edge_case39(self):
        self.assertTrue(check_abundant(432))

    def test_edge_case40(self):
        self.assertFalse(check_abundant(47))

    def test_edge_case41(self):
        self.assertTrue(check_abundant(456))

    def test_edge_case42(self):
        self.assertFalse(check_abundant(49))

    def test_edge_case43(self):
        self.assertTrue(check_abundant(480))

    def test_edge_case44(self):
        self.assertFalse(check_abundant(51))

    def test_edge_case45(self):
        self.assertTrue(check_abundant(504))

    def test_edge_case46(self):
        self.assertFalse(check_abundant(53))

    def test_edge_case47(self):
        self.assertTrue(check_abundant(528))

    def test_edge_case48(self):
        self.assertFalse(check_abundant(55))

    def test_edge_case49(self):
        self.assertTrue(check_abundant(552))

    def test_edge_case50(self):
        self.assertFalse(check_abundant(57))

    def test_edge_case51(self):
        self.assertTrue(check_abundant(576))

    def test_edge_case52(self):
        self.assertFalse(check_abundant(59))

    def test_edge_case53(self):
        self.assertTrue(check_abundant(600))

    def test_edge_case54(self):
        self