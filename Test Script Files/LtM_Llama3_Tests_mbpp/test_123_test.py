import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(amicable_numbers_sum(10), 24)

    def test_edge_case_limit_1(self):
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")

    def test_edge_case_limit_0(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_edge_case_non_integer_input(self):
        self.assertEqual(amicable_numbers_sum("abc"), "Input is not an integer!")

    def test_edge_case_negative_input(self):
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")

    def test_edge_case_limit_2(self):
        self.assertEqual(amicable_numbers_sum(2), 2)

    def test_edge_case_limit_3(self):
        self.assertEqual(amicable_numbers_sum(3), 3)

    def test_edge_case_limit_4(self):
        self.assertEqual(amicable_numbers_sum(4), 3)

    def test_edge_case_limit_5(self):
        self.assertEqual(amicable_numbers_sum(5), 6)

    def test_edge_case_limit_6(self):
        self.assertEqual(amicable_numbers_sum(6), 6)

    def test_edge_case_limit_7(self):
        self.assertEqual(amicable_numbers_sum(7), 8)

    def test_edge_case_limit_8(self):
        self.assertEqual(amicable_numbers_sum(8), 8)

    def test_edge_case_limit_9(self):
        self.assertEqual(amicable_numbers_sum(9), 10)

    def test_edge_case_limit_10(self):
        self.assertEqual(amicable_numbers_sum(10), 24)

    def test_edge_case_limit_11(self):
        self.assertEqual(amicable_numbers_sum(11), 12)

    def test_edge_case_limit_12(self):
        self.assertEqual(amicable_numbers_sum(12), 12)

    def test_edge_case_limit_13(self):
        self.assertEqual(amicable_numbers_sum(13), 14)

    def test_edge_case_limit_14(self):
        self.assertEqual(amicable_numbers_sum(14), 18)

    def test_edge_case_limit_15(self):
        self.assertEqual(amicable_numbers_sum(15), 20)

    def test_edge_case_limit_16(self):
        self.assertEqual(amicable_numbers_sum(16), 20)

    def test_edge_case_limit_17(self):
        self.assertEqual(amicable_numbers_sum(17), 22)

    def test_edge_case_limit_18(self):
        self.assertEqual(amicable_numbers_sum(18), 24)

    def test_edge_case_limit_19(self):
        self.assertEqual(amicable_numbers_sum(19), 26)

    def test_edge_case_limit_20(self):
        self.assertEqual(amicable_numbers_sum(20), 28)
