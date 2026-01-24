import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_edge_case(self):
        self.assertEqual(sum_Of_Primes(1), 0)

    def test_edge_case2(self):
        self.assertEqual(sum_Of_Primes(2), 2)

    def test_edge_case3(self):
        self.assertEqual(sum_Of_Primes(3), 2)

    def test_edge_case4(self):
        self.assertEqual(sum_Of_Primes(4), 2)

    def test_edge_case5(self):
        self.assertEqual(sum_Of_Primes(5), 10)

    def test_edge_case6(self):
        self.assertEqual(sum_Of_Primes(6), 10)

    def test_edge_case7(self):
        self.assertEqual(sum_Of_Primes(7), 10)

    def test_edge_case8(self):
        self.assertEqual(sum_Of_Primes(8), 10)

    def test_edge_case9(self):
        self.assertEqual(sum_Of_Primes(9), 17)

    def test_edge_case10(self):
        self.assertEqual(sum_Of_Primes(10), 17)

    def test_edge_case11(self):
        self.assertEqual(sum_Of_Primes(11), 18)

    def test_edge_case12(self):
        self.assertEqual(sum_Of_Primes(12), 28)

    def test_edge_case13(self):
        self.assertEqual(sum_Of_Primes(13), 28)

    def test_edge_case14(self):
        self.assertEqual(sum_Of_Primes(14), 28)

    def test_edge_case15(self):
        self.assertEqual(sum_Of_Primes(15), 28)

    def test_edge_case16(self):
        self.assertEqual(sum_Of_Primes(16), 28)

    def test_edge_case17(self):
        self.assertEqual(sum_Of_Primes(17), 28)

    def test_edge_case18(self):
        self.assertEqual(sum_Of_Primes(18), 44)

    def test_edge_case19(self):
        self.assertEqual(sum_Of_Primes(19), 44)

    def test_edge_case20(self):
        self.assertEqual(sum_Of_Primes(20), 44)

    def test_edge_case21(self):
        self.assertEqual(sum_Of_Primes(21), 44)

    def test_edge_case22(self):
        self.assertEqual(sum_Of_Primes(22), 44)

    def test_edge_case23(self):
        self.assertEqual(sum_Of_Primes(23), 44)

    def test_edge_case24(self):
        self.assertEqual(sum_Of_Primes(24), 44)

    def test_edge_case25(self):
        self.assertEqual(sum_Of_Primes(25), 44)

    def test_edge_case26(self):
        self.assertEqual(sum_Of_Primes(26), 44)

    def test_edge_case27(self):
        self.assertEqual(sum_Of_Primes(27), 44)

    def test_edge_case28(self):
        self.assertEqual(sum_Of_Primes(28), 44)

    def test_edge_case29(self):
        self.assertEqual(sum_Of_Primes(29), 44)

    def test_edge_case30(self):
        self.assertEqual(sum_Of_Primes(30), 44)
