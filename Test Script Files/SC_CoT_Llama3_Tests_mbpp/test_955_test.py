import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_typical_abundant(self):
        self.assertTrue(is_abundant(12))

    def test_typical_non_abundant(self):
        self.assertFalse(is_abundant(5))

    def test_edge_case_1(self):
        self.assertTrue(is_abundant(1))

    def test_edge_case_2(self):
        self.assertFalse(is_abundant(2))

    def test_edge_case_3(self):
        self.assertFalse(is_abundant(3))

    def test_edge_case_4(self):
        self.assertFalse(is_abundant(4))

    def test_edge_case_5(self):
        self.assertTrue(is_abundant(6))

    def test_edge_case_6(self):
        self.assertFalse(is_abundant(7))

    def test_edge_case_7(self):
        self.assertFalse(is_abundant(8))

    def test_edge_case_8(self):
        self.assertFalse(is_abundant(9))

    def test_edge_case_9(self):
        self.assertFalse(is_abundant(10))

    def test_edge_case_10(self):
        self.assertTrue(is_abundant(12))

    def test_edge_case_11(self):
        self.assertFalse(is_abundant(13))

    def test_edge_case_12(self):
        self.assertFalse(is_abundant(14))

    def test_edge_case_13(self):
        self.assertFalse(is_abundant(15))

    def test_edge_case_14(self):
        self.assertFalse(is_abundant(16))

    def test_edge_case_15(self):
        self.assertTrue(is_abundant(18))

    def test_edge_case_16(self):
        self.assertFalse(is_abundant(19))

    def test_edge_case_17(self):
        self.assertFalse(is_abundant(20))

    def test_edge_case_18(self):
        self.assertFalse(is_abundant(21))

    def test_edge_case_19(self):
        self.assertFalse(is_abundant(22))

    def test_edge_case_20(self):
        self.assertFalse(is_abundant(23))

    def test_edge_case_21(self):
        self.assertFalse(is_abundant(24))

    def test_edge_case_22(self):
        self.assertFalse(is_abundant(25))

    def test_edge_case_23(self):
        self.assertFalse(is_abundant(26))

    def test_edge_case_24(self):
        self.assertFalse(is_abundant(27))

    def test_edge_case_25(self):
        self.assertFalse(is_abundant(28))

    def test_edge_case_26(self):
        self.assertFalse(is_abundant(29))

    def test_edge_case_27(self):
        self.assertFalse(is_abundant(30))

    def test_edge_case_28(self):
        self.assertFalse(is_abundant(31))

    def test_edge_case_29(self):
        self.assertFalse(is_abundant(32))

    def test_edge_case_30(self):
        self.assertFalse(is_abundant(33))

    def test_edge_case_31(self):
        self.assertFalse(is_abundant(34))

    def test_edge_case_32(self):
        self.assertFalse(is_abundant(35))

    def test_edge_case_33(self):
        self.assertFalse(is_abundant(36))

    def test_edge_case_34(self):
        self.assertFalse(is_abundant(37))

    def test_edge_case_35(self):
        self.assertFalse(is_abundant(38))

    def test_edge_case_36(self):
        self.assertFalse(is_abundant(39))

    def test_edge_case_37(self):
        self.assertFalse(is_abundant(40))

    def test_edge_case_38(self):
        self.assertFalse(is_abundant(41))

    def test_edge_case_39(self):
        self.assertFalse(is_abundant(42))

    def test_edge_case_40(self):
        self.assertFalse(is_abundant(43))

    def test_edge_case_41(self):
        self.assertFalse(is_abundant(44))

    def test_edge_case_42(self):
        self.assertFalse(is_abundant(45))

    def test_edge_case_43(self):
        self.assertFalse(is_abundant(46))

    def test_edge_case_44(self):
        self.assertFalse(is_abundant(47))

    def test_edge_case_45(self):
        self.assertFalse(is_abundant(48))

    def test_edge_case_46(self):
        self.assertFalse(is_abundant(49))

    def test_edge_case_47(self):
        self.assertFalse(is_abundant(50))

    def test_edge_case_48(self):
        self.assertFalse(is_abundant(51))

    def test_edge_case_49(self):
        self.assertFalse(is_abundant(52))

    def test_edge_case_50(self):
        self.assertFalse(is_abundant(53))

    def test_edge_case_51(self):
        self