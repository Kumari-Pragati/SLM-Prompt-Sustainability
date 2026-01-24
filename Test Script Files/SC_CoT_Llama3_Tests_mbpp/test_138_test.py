import unittest
from mbpp_138_code import is_Sum_Of_Powers_Of_Two

class TestIsSumOfPowersOfTwo(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(4))

    def test_edge_case(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))

    def test_edge_case2(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(5))

    def test_edge_case3(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(0))

    def test_edge_case4(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(1))

    def test_edge_case5(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(3))

    def test_edge_case6(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(6))

    def test_edge_case7(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(7))

    def test_edge_case8(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(8))

    def test_edge_case9(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(9))

    def test_edge_case10(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(12))

    def test_edge_case11(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(13))

    def test_edge_case12(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(16))

    def test_edge_case13(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(17))

    def test_edge_case14(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(20))

    def test_edge_case15(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(21))

    def test_edge_case16(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(24))

    def test_edge_case17(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(25))

    def test_edge_case18(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(28))

    def test_edge_case19(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(29))

    def test_edge_case20(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(32))

    def test_edge_case21(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(33))

    def test_edge_case22(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(36))

    def test_edge_case23(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(37))

    def test_edge_case24(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(40))

    def test_edge_case25(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(41))

    def test_edge_case26(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(44))

    def test_edge_case27(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(45))

    def test_edge_case28(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(48))

    def test_edge_case29(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(49))

    def test_edge_case30(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(52))

    def test_edge_case31(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(53))

    def test_edge_case32(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(56))

    def test_edge_case33(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(57))

    def test_edge_case34(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(60))

    def test_edge_case35(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(61))

    def test_edge_case36(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(64))

    def test_edge_case37(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(65))

    def test_edge_case38(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(68))

    def test_edge_case39(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(69))

    def test_edge_case40(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(72))

    def test_edge_case41(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(73))

    def test_edge_case42(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(76))

    def test_edge_case43(self):
        self.assertFalse(is_Sum_Of_Powers_Of_Two(77))

    def test_edge_case44(self):
        self.assertTrue(is_Sum_Of_Powers_Of_Two(80))

    def test_edge_case45