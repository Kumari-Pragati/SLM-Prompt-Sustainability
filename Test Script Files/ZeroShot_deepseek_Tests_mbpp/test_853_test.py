import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_sum_of_odd_factors_1(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_sum_of_odd_factors_2(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_sum_of_odd_factors_3(self):
        self.assertEqual(sum_of_odd_Factors(3), 4)

    def test_sum_of_odd_factors_4(self):
        self.assertEqual(sum_of_odd_Factors(4), 6)

    def test_sum_of_odd_factors_5(self):
        self.assertEqual(sum_of_odd_Factors(5), 6)

    def test_sum_of_odd_factors_6(self):
        self.assertEqual(sum_of_odd_Factors(6), 10)

    def test_sum_of_odd_factors_7(self):
        self.assertEqual(sum_of_odd_Factors(7), 8)

    def test_sum_of_odd_factors_8(self):
        self.assertEqual(sum_of_odd_Factors(8), 15)

    def test_sum_of_odd_factors_9(self):
        self.assertEqual(sum_of_odd_Factors(9), 16)

    def test_sum_of_odd_factors_10(self):
        self.assertEqual(sum_of_odd_Factors(10), 18)

    def test_sum_of_odd_factors_11(self):
        self.assertEqual(sum_of_odd_Factors(11), 20)

    def test_sum_of_odd_factors_12(self):
        self.assertEqual(sum_of_odd_Factors(12), 28)

    def test_sum_of_odd_factors_13(self):
        self.assertEqual(sum_of_odd_Factors(13), 24)

    def test_sum_of_odd_factors_14(self):
        self.assertEqual(sum_of_odd_Factors(14), 30)

    def test_sum_of_odd_factors_15(self):
        self.assertEqual(sum_of_odd_Factors(15), 33)

    def test_sum_of_odd_factors_16(self):
        self.assertEqual(sum_of_odd_Factors(16), 45)

    def test_sum_of_odd_factors_17(self):
        self.assertEqual(sum_of_odd_Factors(17), 40)

    def test_sum_of_odd_factors_18(self):
        self.assertEqual(sum_of_odd_Factors(18), 46)

    def test_sum_of_odd_factors_19(self):
        self.assertEqual(sum_of_odd_Factors(19), 48)

    def test_sum_of_odd_factors_20(self):
        self.assertEqual(sum_of_odd_Factors(20), 57)
