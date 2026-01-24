import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_invalid_input1(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input2(self):
        self.assertFalse(check_Validity(2, 2, 1))

    def test_invalid_input3(self):
        self.assertFalse(check_Validity(1, 3, 2))

    def test_invalid_input4(self):
        self.assertFalse(check_Validity(3, 1, 2))

    def test_invalid_input5(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input6(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input7(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input8(self):
        self.assertFalse(check_Validity(2, 2, 2))

    def test_invalid_input9(self):
        self.assertFalse(check_Validity(1, 3, 3))

    def test_invalid_input10(self):
        self.assertFalse(check_Validity(3, 1, 3))

    def test_invalid_input11(self):
        self.assertFalse(check_Validity(1, 2, 3))

    def test_invalid_input12(self):
        self.assertFalse(check_Validity(2, 3, 1))

    def test_invalid_input13(self):
        self.assertFalse(check_Validity(1, 1, 3))

    def test_invalid_input14(self):
        self.assertFalse(check_Validity(2, 1, 3))

    def test_invalid_input15(self):
        self.assertFalse(check_Validity(1, 2, 2))

    def test_invalid_input16(self):
        self.assertFalse(check_Validity(2, 2, 3))

    def test_invalid_input17(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input18(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input19(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input20(self):
        self.assertFalse(check_Validity(2, 3, 2))

    def test_invalid_input21(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input22(self):
        self.assertFalse(check_Validity(2, 2, 1))

    def test_invalid_input23(self):
        self.assertFalse(check_Validity(1, 3, 1))

    def test_invalid_input24(self):
        self.assertFalse(check_Validity(2, 1, 2))

    def test_invalid_input25(self):
        self.assertFalse(check_Validity(1, 2, 2))

    def test_invalid_input26(self):
        self.assertFalse(check_Validity(2, 3, 3))

    def test_invalid_input27(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input28(self):
        self.assertFalse(check_Validity(2, 1, 2))

    def test_invalid_input29(self):
        self.assertFalse(check_Validity(1, 2, 3))

    def test_invalid_input30(self):
        self.assertFalse(check_Validity(2, 3, 1))

    def test_invalid_input31(self):
        self.assertFalse(check_Validity(1, 1, 3))

    def test_invalid_input32(self):
        self.assertFalse(check_Validity(2, 1, 3))

    def test_invalid_input33(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input34(self):
        self.assertFalse(check_Validity(2, 2, 1))

    def test_invalid_input35(self):
        self.assertFalse(check_Validity(1, 3, 2))

    def test_invalid_input36(self):
        self.assertFalse(check_Validity(2, 3, 2))

    def test_invalid_input37(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input38(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input39(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input40(self):
        self.assertFalse(check_Validity(2, 2, 2))

    def test_invalid_input41(self):
        self.assertFalse(check_Validity(1, 3, 3))

    def test_invalid_input42(self):
        self.assertFalse(check_Validity(2, 1, 3))

    def test_invalid_input43(self):
        self.assertFalse(check_Validity(1,