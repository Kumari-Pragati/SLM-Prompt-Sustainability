import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_edge_case_limit_1(self):
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")

    def test_edge_case_limit_0(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_edge_case_limit_negative(self):
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")

    def test_edge_case_limit_non_integer(self):
        self.assertEqual(amicable_numbers_sum("abc"), "Input is not an integer!")

    def test_edge_case_limit_non_integer2(self):
        self.assertEqual(amicable_numbers_sum(1.5), "Input is not an integer!")

    def test_edge_case_limit_non_integer3(self):
        self.assertEqual(amicable_numbers_sum([1, 2, 3]), "Input is not an integer!")
