import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_edge_case_limit_1(self):
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")

    def test_edge_case_limit_0(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_invalid_input_non_integer(self):
        self.assertEqual(amicable_numbers_sum("hello"), "Input is not an integer!")

    def test_edge_case_limit_2(self):
        self.assertEqual(amicable_numbers_sum(2), 0)

    def test_edge_case_limit_3(self):
        self.assertEqual(amicable_numbers_sum(3), 0)

    def test_edge_case_limit_4(self):
        self.assertEqual(amicable_numbers_sum(4), 2)

    def test_edge_case_limit_5(self):
        self.assertEqual(amicable_numbers_sum(5), 2)

    def test_edge_case_limit_6(self):
        self.assertEqual(amicable_numbers_sum(6), 6)

    def test_edge_case_limit_7(self):
        self.assertEqual(amicable_numbers_sum(7), 2)

    def test_edge_case_limit_8(self):
        self.assertEqual(amicable_numbers_sum(8), 8)

    def test_edge_case_limit_9(self):
        self.assertEqual(amicable_numbers_sum(9), 6)

    def test_edge_case_limit_10(self):
        self.assertEqual(amicable_numbers_sum(10), 8)
