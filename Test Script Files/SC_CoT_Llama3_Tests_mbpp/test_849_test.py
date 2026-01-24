import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_sum_of_primes(self):
        self.assertEqual(Sum(10), 17)

    def test_sum_of_primes_edge_case(self):
        self.assertEqual(Sum(2), 0)

    def test_sum_of_primes_edge_case2(self):
        self.assertEqual(Sum(1), 0)

    def test_sum_of_primes_edge_case3(self):
        self.assertEqual(Sum(0), 0)

    def test_sum_of_primes_edge_case4(self):
        self.assertEqual(Sum(-1), 0)

    def test_sum_of_primes_edge_case5(self):
        self.assertEqual(Sum(5), 6)

    def test_sum_of_primes_edge_case6(self):
        self.assertEqual(Sum(7), 10)

    def test_sum_of_primes_edge_case7(self):
        self.assertEqual(Sum(11), 15)

    def test_sum_of_primes_edge_case8(self):
        self.assertEqual(Sum(12), 16)

    def test_sum_of_primes_edge_case9(self):
        self.assertEqual(Sum(13), 18)

    def test_sum_of_primes_edge_case10(self):
        self.assertEqual(Sum(14), 18)

    def test_sum_of_primes_edge_case11(self):
        self.assertEqual(Sum(15), 18)

    def test_sum_of_primes_edge_case12(self):
        self.assertEqual(Sum(16), 20)

    def test_sum_of_primes_edge_case13(self):
        self.assertEqual(Sum(17), 21)

    def test_sum_of_primes_edge_case14(self):
        self.assertEqual(Sum(18), 22)

    def test_sum_of_primes_edge_case15(self):
        self.assertEqual(Sum(19), 23)

    def test_sum_of_primes_edge_case16(self):
        self.assertEqual(Sum(20), 24)

    def test_sum_of_primes_edge_case17(self):
        self.assertEqual(Sum(21), 25)

    def test_sum_of_primes_edge_case18(self):
        self.assertEqual(Sum(22), 26)

    def test_sum_of_primes_edge_case19(self):
        self.assertEqual(Sum(23), 27)

    def test_sum_of_primes_edge_case20(self):
        self.assertEqual(Sum(24), 28)

    def test_sum_of_primes_edge_case21(self):
        self.assertEqual(Sum(25), 29)

    def test_sum_of_primes_edge_case22(self):
        self.assertEqual(Sum(26), 30)

    def test_sum_of_primes_edge_case23(self):
        self.assertEqual(Sum(27), 31)

    def test_sum_of_primes_edge_case24(self):
        self.assertEqual(Sum(28), 32)

    def test_sum_of_primes_edge_case25(self):
        self.assertEqual(Sum(29), 33)

    def test_sum_of_primes_edge_case26(self):
        self.assertEqual(Sum(30), 34)

    def test_sum_of_primes_edge_case27(self):
        self.assertEqual(Sum(31), 35)

    def test_sum_of_primes_edge_case28(self):
        self.assertEqual(Sum(32), 36)

    def test_sum_of_primes_edge_case29(self):
        self.assertEqual(Sum(33), 37)

    def test_sum_of_primes_edge_case30(self):
        self.assertEqual(Sum(34), 38)

    def test_sum_of_primes_edge_case31(self):
        self.assertEqual(Sum(35), 39)

    def test_sum_of_primes_edge_case32(self):
        self.assertEqual(Sum(36), 40)

    def test_sum_of_primes_edge_case33(self):
        self.assertEqual(Sum(37), 41)

    def test_sum_of_primes_edge_case34(self):
        self.assertEqual(Sum(38), 42)

    def test_sum_of_primes_edge_case35(self):
        self.assertEqual(Sum(39), 43)

    def test_sum_of_primes_edge_case36(self):
        self.assertEqual(Sum(40), 44)

    def test_sum_of_primes_edge_case37(self):
        self.assertEqual(Sum(41), 45)

    def test_sum_of_primes_edge_case38(self):
        self.assertEqual(Sum(42), 46)

    def test_sum_of_primes_edge_case39(self):
        self.assertEqual(Sum(43), 47)

    def test_sum_of_primes_edge_case40(self):
        self.assertEqual(Sum(44), 48)

    def test_sum_of_primes_edge_case41(self):
        self.assertEqual(Sum(45), 49)

    def test_sum_of_primes_edge_case42(self):
        self.assertEqual(Sum(46), 50)

    def test_sum_of_primes_edge_case43(self):
        self.assertEqual(Sum(47), 51)