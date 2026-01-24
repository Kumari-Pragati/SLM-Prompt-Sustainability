import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check("101"), "Yes")

    def test_edge_case1(self):
        self.assertEqual(check("0"), "Yes")

    def test_edge_case2(self):
        self.assertEqual(check("1"), "Yes")

    def test_edge_case3(self):
        self.assertEqual(check("111"), "Yes")

    def test_edge_case4(self):
        self.assertEqual(check("000"), "Yes")

    def test_edge_case5(self):
        self.assertEqual(check("01"), "No")

    def test_edge_case6(self):
        self.assertEqual(check("10"), "No")

    def test_edge_case7(self):
        self.assertEqual(check("110"), "No")

    def test_edge_case8(self):
        self.assertEqual(check("001"), "No")

    def test_edge_case9(self):
        self.assertEqual(check("100"), "No")

    def test_edge_case10(self):
        self.assertEqual(check("1111"), "Yes")

    def test_edge_case11(self):
        self.assertEqual(check("0000"), "Yes")

    def test_edge_case12(self):
        self.assertEqual(check("1010"), "No")

    def test_edge_case13(self):
        self.assertEqual(check("0101"), "No")

    def test_edge_case14(self):
        self.assertEqual(check("1011"), "No")

    def test_edge_case15(self):
        self.assertEqual(check("0110"), "No")

    def test_edge_case16(self):
        self.assertEqual(check("1001"), "No")

    def test_edge_case17(self):
        self.assertEqual(check("1100"), "No")

    def test_edge_case18(self):
        self.assertEqual(check("0011"), "No")

    def test_edge_case19(self):
        self.assertEqual(check("1110"), "No")

    def test_edge_case20(self):
        self.assertEqual(check("0001"), "No")

    def test_edge_case21(self):
        self.assertEqual(check("10101"), "No")

    def test_edge_case22(self):
        self.assertEqual(check("01010"), "No")

    def test_edge_case23(self):
        self.assertEqual(check("10110"), "No")

    def test_edge_case24(self):
        self.assertEqual(check("01101"), "No")

    def test_edge_case25(self):
        self.assertEqual(check("10010"), "No")

    def test_edge_case26(self):
        self.assertEqual(check("11010"), "No")

    def test_edge_case27(self):
        self.assertEqual(check("00110"), "No")

    def test_edge_case28(self):
        self.assertEqual(check("11110"), "No")

    def test_edge_case29(self):
        self.assertEqual(check("00010"), "No")

    def test_edge_case30(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case31(self):
        self.assertEqual(check("01011"), "No")

    def test_edge_case32(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case33(self):
        self.assertEqual(check("01111"), "No")

    def test_edge_case34(self):
        self.assertEqual(check("10011"), "No")

    def test_edge_case35(self):
        self.assertEqual(check("11011"), "No")

    def test_edge_case36(self):
        self.assertEqual(check("00111"), "No")

    def test_edge_case37(self):
        self.assertEqual(check("11111"), "Yes")

    def test_edge_case38(self):
        self.assertEqual(check("00011"), "No")

    def test_edge_case39(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case40(self):
        self.assertEqual(check("01011"), "No")

    def test_edge_case41(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case42(self):
        self.assertEqual(check("01111"), "No")

    def test_edge_case43(self):
        self.assertEqual(check("10011"), "No")

    def test_edge_case44(self):
        self.assertEqual(check("11011"), "No")

    def test_edge_case45(self):
        self.assertEqual(check("00111"), "No")

    def test_edge_case46(self):
        self.assertEqual(check("11111"), "Yes")

    def test_edge_case47(self):
        self.assertEqual(check("00011"), "No")

    def test_edge_case48(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case49(self):
        self.assertEqual(check("01011"), "No")

    def test_edge_case50(self):
        self.assertEqual(check("10111"), "No")

    def test_edge_case51(self):
        self.assertEqual(check("01111"), "No")

    def test_edge_case52(self):
        self.assertEqual(check("10011"), "No")

    def test_edge_case53(self):