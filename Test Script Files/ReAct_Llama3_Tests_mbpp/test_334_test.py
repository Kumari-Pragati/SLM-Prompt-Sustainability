import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_invalid_input1(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input2(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input3(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input4(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input5(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input6(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input7(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input8(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input9(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input10(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input11(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input12(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input13(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input14(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input15(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input16(self):
        self.assertFalse(check_Validity(2, 1, 1))

    def test_invalid_input17(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_invalid_input18(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_invalid_input19(self):
        self.assertFalse(check_Validity(1, 1, 2))

    def test_invalid_input20(self):
        self.assertFalse(check_Validity(2, 1, 1))
