import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(10000), 3168)

    def test_edge_case_limit_1(self):
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")

    def test_edge_case_limit_0(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_edge_case_non_integer_input(self):
        self.assertEqual(amicable_numbers_sum("abc"), "Input is not an integer!")

    def test_edge_case_negative_input(self):
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")

    def test_edge_case_zero_input(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
