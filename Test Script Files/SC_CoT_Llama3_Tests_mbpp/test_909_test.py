import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(previous_palindrome(10), 9)

    def test_edge_case(self):
        self.assertEqual(previous_palindrome(1), None)

    def test_edge_case2(self):
        self.assertEqual(previous_palindrome(0), None)

    def test_edge_case3(self):
        self.assertEqual(previous_palindrome(2), 1)

    def test_edge_case4(self):
        self.assertEqual(previous_palindrome(11), 10)

    def test_edge_case5(self):
        self.assertEqual(previous_palindrome(12), 11)

    def test_edge_case6(self):
        self.assertEqual(previous_palindrome(13), 12)

    def test_edge_case7(self):
        self.assertEqual(previous_palindrome(14), 13)

    def test_edge_case8(self):
        self.assertEqual(previous_palindrome(15), 14)

    def test_edge_case9(self):
        self.assertEqual(previous_palindrome(16), 15)

    def test_edge_case10(self):
        self.assertEqual(previous_palindrome(17), 16)

    def test_edge_case11(self):
        self.assertEqual(previous_palindrome(18), 17)

    def test_edge_case12(self):
        self.assertEqual(previous_palindrome(19), 18)

    def test_edge_case13(self):
        self.assertEqual(previous_palindrome(20), 19)

    def test_edge_case14(self):
        self.assertEqual(previous_palindrome(21), 20)

    def test_edge_case15(self):
        self.assertEqual(previous_palindrome(22), 21)

    def test_edge_case16(self):
        self.assertEqual(previous_palindrome(23), 22)

    def test_edge_case17(self):
        self.assertEqual(previous_palindrome(24), 23)

    def test_edge_case18(self):
        self.assertEqual(previous_palindrome(25), 24)

    def test_edge_case19(self):
        self.assertEqual(previous_palindrome(26), 25)

    def test_edge_case20(self):
        self.assertEqual(previous_palindrome(27), 26)

    def test_edge_case21(self):
        self.assertEqual(previous_palindrome(28), 27)

    def test_edge_case22(self):
        self.assertEqual(previous_palindrome(29), 28)

    def test_edge_case23(self):
        self.assertEqual(previous_palindrome(30), 29)

    def test_edge_case24(self):
        self.assertEqual(previous_palindrome(31), 30)

    def test_edge_case25(self):
        self.assertEqual(previous_palindrome(32), 31)

    def test_edge_case26(self):
        self.assertEqual(previous_palindrome(33), 32)

    def test_edge_case27(self):
        self.assertEqual(previous_palindrome(34), 33)

    def test_edge_case28(self):
        self.assertEqual(previous_palindrome(35), 34)

    def test_edge_case29(self):
        self.assertEqual(previous_palindrome(36), 35)

    def test_edge_case30(self):
        self.assertEqual(previous_palindrome(37), 36)

    def test_edge_case31(self):
        self.assertEqual(previous_palindrome(38), 37)

    def test_edge_case32(self):
        self.assertEqual(previous_palindrome(39), 38)

    def test_edge_case33(self):
        self.assertEqual(previous_palindrome(40), 39)

    def test_edge_case34(self):
        self.assertEqual(previous_palindrome(41), 40)

    def test_edge_case35(self):
        self.assertEqual(previous_palindrome(42), 41)

    def test_edge_case36(self):
        self.assertEqual(previous_palindrome(43), 42)

    def test_edge_case37(self):
        self.assertEqual(previous_palindrome(44), 43)

    def test_edge_case38(self):
        self.assertEqual(previous_palindrome(45), 44)

    def test_edge_case39(self):
        self.assertEqual(previous_palindrome(46), 45)

    def test_edge_case40(self):
        self.assertEqual(previous_palindrome(47), 46)

    def test_edge_case41(self):
        self.assertEqual(previous_palindrome(48), 47)

    def test_edge_case42(self):
        self.assertEqual(previous_palindrome(49), 48)

    def test_edge_case43(self):
        self.assertEqual(previous_palindrome(50), 49)

    def test_edge_case44(self):
        self.assertEqual(previous_palindrome(51), 50)

    def test_edge_case45(self):
        self.assertEqual(previous_palindrome(52), 51)

    def test_edge_case46(self):
        self.assertEqual(previous_palindrome(53), 52)

    def test_edge_case47(self):
        self.assertEqual(previous_palindrome(54), 53)

    def test_edge_case48(self):
        self.assertEqual(previous_palindrome(55), 54)

    def test_edge_case49(self):
        self.assertEqual(previous_palindrome(56), 55)

    def test_edge_case50(self):