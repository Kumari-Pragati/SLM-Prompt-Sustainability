import unittest
from mbpp_711_code import product_Equal

class TestProductEqual(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(product_Equal(123456789))

    def test_edge_case_1(self):
        self.assertFalse(product_Equal(9))

    def test_edge_case_2(self):
        self.assertTrue(product_Equal(111111111))

    def test_edge_case_3(self):
        self.assertFalse(product_Equal(1234567890))

    def test_edge_case_4(self):
        self.assertTrue(product_Equal(222222222))

    def test_edge_case_5(self):
        self.assertFalse(product_Equal(12345678901))

    def test_edge_case_6(self):
        self.assertTrue(product_Equal(333333333))

    def test_edge_case_7(self):
        self.assertFalse(product_Equal(12345678902))

    def test_edge_case_8(self):
        self.assertTrue(product_Equal(444444444))

    def test_edge_case_9(self):
        self.assertFalse(product_Equal(12345678903))

    def test_edge_case_10(self):
        self.assertTrue(product_Equal(555555555))

    def test_edge_case_11(self):
        self.assertFalse(product_Equal(12345678904))

    def test_edge_case_12(self):
        self.assertTrue(product_Equal(666666666))

    def test_edge_case_13(self):
        self.assertFalse(product_Equal(12345678905))

    def test_edge_case_14(self):
        self.assertTrue(product_Equal(777777777))

    def test_edge_case_15(self):
        self.assertFalse(product_Equal(12345678906))

    def test_edge_case_16(self):
        self.assertTrue(product_Equal(888888888))

    def test_edge_case_17(self):
        self.assertFalse(product_Equal(12345678907))

    def test_edge_case_18(self):
        self.assertTrue(product_Equal(999999999))

    def test_edge_case_19(self):
        self.assertFalse(product_Equal(12345678908))

    def test_edge_case_20(self):
        self.assertTrue(product_Equal(111111111111))

    def test_edge_case_21(self):
        self.assertFalse(product_Equal(12345678909))

    def test_edge_case_22(self):
        self.assertTrue(product_Equal(222222222222))

    def test_edge_case_23(self):
        self.assertFalse(product_Equal(12345678910))

    def test_edge_case_24(self):
        self.assertTrue(product_Equal(333333333333))

    def test_edge_case_25(self):
        self.assertFalse(product_Equal(12345678911))

    def test_edge_case_26(self):
        self.assertTrue(product_Equal(444444444444))

    def test_edge_case_27(self):
        self.assertFalse(product_Equal(12345678912))

    def test_edge_case_28(self):
        self.assertTrue(product_Equal(555555555555))

    def test_edge_case_29(self):
        self.assertFalse(product_Equal(12345678913))

    def test_edge_case_30(self):
        self.assertTrue(product_Equal(666666666666))

    def test_edge_case_31(self):
        self.assertFalse(product_Equal(12345678914))

    def test_edge_case_32(self):
        self.assertTrue(product_Equal(777777777777))

    def test_edge_case_33(self):
        self.assertFalse(product_Equal(12345678915))

    def test_edge_case_34(self):
        self.assertTrue(product_Equal(888888888888))

    def test_edge_case_35(self):
        self.assertFalse(product_Equal(12345678916))

    def test_edge_case_36(self):
        self.assertTrue(product_Equal(999999999999))

    def test_edge_case_37(self):
        self.assertFalse(product_Equal(12345678917))

    def test_edge_case_38(self):
        self.assertTrue(product_Equal(11111111111111))

    def test_edge_case_39(self):
        self.assertFalse(product_Equal(12345678918))

    def test_edge_case_40(self):
        self.assertTrue(product_Equal(22222222222222))

    def test_edge_case_41(self):
        self.assertFalse(product_Equal(12345678919))

    def test_edge_case_42(self):
        self.assertTrue(product_Equal(33333333333333))

    def test_edge_case_43(self):
        self.assertFalse(product_Equal(12345678920))

    def test_edge_case_44(self):
        self.assertTrue(product_Equal(44444444444444))

    def test_edge_case_45(self):
        self.assertFalse(product_Equal(12345678921))

    def test_edge_case_46(self):
        self.assertTrue(product_Equal(55555555555555))

    def test_edge_case_47(self):
        self.assertFalse(product_Equal(12345678922))

    def test_edge