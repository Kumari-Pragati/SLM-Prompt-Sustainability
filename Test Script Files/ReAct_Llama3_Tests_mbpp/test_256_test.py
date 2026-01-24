import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_one(self):
        self.assertEqual(count_Primes_nums(1), 0)

    def test_two(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_small(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_large(self):
        self.assertEqual(count_Primes_nums(100), 23)

    def test_edge_case(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Primes_nums(3), 2)

    def test_edge_case3(self):
        self.assertEqual(count_Primes_nums(4), 2)

    def test_edge_case4(self):
        self.assertEqual(count_Primes_nums(5), 3)

    def test_edge_case5(self):
        self.assertEqual(count_Primes_nums(6), 3)

    def test_edge_case6(self):
        self.assertEqual(count_Primes_nums(7), 4)

    def test_edge_case7(self):
        self.assertEqual(count_Primes_nums(8), 4)

    def test_edge_case8(self):
        self.assertEqual(count_Primes_nums(9), 4)

    def test_edge_case9(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_edge_case10(self):
        self.assertEqual(count_Primes_nums(11), 5)

    def test_edge_case11(self):
        self.assertEqual(count_Primes_nums(12), 5)

    def test_edge_case12(self):
        self.assertEqual(count_Primes_nums(13), 6)

    def test_edge_case13(self):
        self.assertEqual(count_Primes_nums(14), 6)

    def test_edge_case14(self):
        self.assertEqual(count_Primes_nums(15), 6)

    def test_edge_case15(self):
        self.assertEqual(count_Primes_nums(16), 6)

    def test_edge_case16(self):
        self.assertEqual(count_Primes_nums(17), 7)

    def test_edge_case17(self):
        self.assertEqual(count_Primes_nums(18), 7)

    def test_edge_case18(self):
        self.assertEqual(count_Primes_nums(19), 8)

    def test_edge_case19(self):
        self.assertEqual(count_Primes_nums(20), 8)

    def test_edge_case20(self):
        self.assertEqual(count_Primes_nums(21), 8)

    def test_edge_case21(self):
        self.assertEqual(count_Primes_nums(22), 8)

    def test_edge_case22(self):
        self.assertEqual(count_Primes_nums(23), 9)

    def test_edge_case23(self):
        self.assertEqual(count_Primes_nums(24), 9)

    def test_edge_case24(self):
        self.assertEqual(count_Primes_nums(25), 9)

    def test_edge_case25(self):
        self.assertEqual(count_Primes_nums(26), 9)

    def test_edge_case26(self):
        self.assertEqual(count_Primes_nums(27), 9)

    def test_edge_case27(self):
        self.assertEqual(count_Primes_nums(28), 9)

    def test_edge_case28(self):
        self.assertEqual(count_Primes_nums(29), 10)

    def test_edge_case29(self):
        self.assertEqual(count_Primes_nums(30), 10)

    def test_edge_case30(self):
        self.assertEqual(count_Primes_nums(31), 10)

    def test_edge_case31(self):
        self.assertEqual(count_Primes_nums(32), 10)

    def test_edge_case32(self):
        self.assertEqual(count_Primes_nums(33), 10)

    def test_edge_case33(self):
        self.assertEqual(count_Primes_nums(34), 10)

    def test_edge_case34(self):
        self.assertEqual(count_Primes_nums(35), 10)

    def test_edge_case35(self):
        self.assertEqual(count_Primes_nums(36), 10)

    def test_edge_case36(self):
        self.assertEqual(count_Primes_nums(37), 11)

    def test_edge_case37(self):
        self.assertEqual(count_Primes_nums(38), 11)

    def test_edge_case38(self):
        self.assertEqual(count_Primes_nums(39), 11)

    def test_edge_case39(self):
        self.assertEqual(count_Primes_nums(40), 11)

    def test_edge_case40(self):
        self.assertEqual(count_Primes_nums(41), 12)

    def test_edge_case41(self):
        self.assertEqual(count_Primes_nums(42), 12)

    def test_edge_case42(self):
        self.assertEqual(count_Primes_nums(43), 12)

    def test_edge_case43(self):
        self.assertEqual(count_Primes_nums(44), 12)

    def