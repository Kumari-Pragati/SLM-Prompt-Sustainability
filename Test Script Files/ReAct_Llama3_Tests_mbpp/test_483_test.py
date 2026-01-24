import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(5), 2)

    def test_edge_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_edge_case2(self):
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)

    def test_edge_case3(self):
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)

    def test_edge_case4(self):
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)

    def test_edge_case5(self):
        self.assertEqual(first_Factorial_Divisible_Number(6), 2)

    def test_edge_case6(self):
        self.assertEqual(first_Factorial_Divisible_Number(7), 3)

    def test_edge_case7(self):
        self.assertEqual(first_Factorial_Divisible_Number(8), 3)

    def test_edge_case8(self):
        self.assertEqual(first_Factorial_Divisible_Number(9), 4)

    def test_edge_case9(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 4)

    def test_edge_case10(self):
        self.assertEqual(first_Factorial_Divisible_Number(11), 5)

    def test_edge_case11(self):
        self.assertEqual(first_Factorial_Divisible_Number(12), 5)

    def test_edge_case12(self):
        self.assertEqual(first_Factorial_Divisible_Number(13), 6)

    def test_edge_case13(self):
        self.assertEqual(first_Factorial_Divisible_Number(14), 6)

    def test_edge_case14(self):
        self.assertEqual(first_Factorial_Divisible_Number(15), 6)

    def test_edge_case15(self):
        self.assertEqual(first_Factorial_Divisible_Number(16), 7)

    def test_edge_case16(self):
        self.assertEqual(first_Factorial_Divisible_Number(17), 7)

    def test_edge_case17(self):
        self.assertEqual(first_Factorial_Divisible_Number(18), 8)

    def test_edge_case18(self):
        self.assertEqual(first_Factorial_Divisible_Number(19), 8)

    def test_edge_case19(self):
        self.assertEqual(first_Factorial_Divisible_Number(20), 8)

    def test_edge_case20(self):
        self.assertEqual(first_Factorial_Divisible_Number(21), 9)

    def test_edge_case21(self):
        self.assertEqual(first_Factorial_Divisible_Number(22), 9)

    def test_edge_case22(self):
        self.assertEqual(first_Factorial_Divisible_Number(23), 9)

    def test_edge_case23(self):
        self.assertEqual(first_Factorial_Divisible_Number(24), 10)

    def test_edge_case24(self):
        self.assertEqual(first_Factorial_Divisible_Number(25), 10)

    def test_edge_case25(self):
        self.assertEqual(first_Factorial_Divisible_Number(26), 10)

    def test_edge_case26(self):
        self.assertEqual(first_Factorial_Divisible_Number(27), 11)

    def test_edge_case27(self):
        self.assertEqual(first_Factorial_Divisible_Number(28), 11)

    def test_edge_case28(self):
        self.assertEqual(first_Factorial_Divisible_Number(29), 11)

    def test_edge_case29(self):
        self.assertEqual(first_Factorial_Divisible_Number(30), 12)

    def test_edge_case30(self):
        self.assertEqual(first_Factorial_Divisible_Number(31), 12)

    def test_edge_case31(self):
        self.assertEqual(first_Factorial_Divisible_Number(32), 12)

    def test_edge_case32(self):
        self.assertEqual(first_Factorial_Divisible_Number(33), 13)

    def test_edge_case33(self):
        self.assertEqual(first_Factorial_Divisible_Number(34), 13)

    def test_edge_case34(self):
        self.assertEqual(first_Factorial_Divisible_Number(35), 13)

    def test_edge_case35(self):
        self.assertEqual(first_Factorial_Divisible_Number(36), 14)

    def test_edge_case36(self):
        self.assertEqual(first_Factorial_Divisible_Number(37), 14)

    def test_edge_case37(self):
        self.assertEqual(first_Factorial_Divisible_Number(38), 14)

    def test_edge_case38(self):
        self.assertEqual(first_Factorial_Divisible_Number(39), 15)

    def test_edge_case39(self):
        self.assertEqual(first_Factorial_Divisible_Number(