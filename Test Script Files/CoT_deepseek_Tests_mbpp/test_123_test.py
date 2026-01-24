import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_input_not_integer(self):
        self.assertEqual(amicable_numbers_sum("string"), "Input is not an integer!")

    def test_input_less_than_1(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(285), 504)

    def test_edge_case_with_small_limit(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_edge_case_with_large_limit(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_invalid_input_type(self):
        self.assertEqual(amicable_numbers_sum(None), "Input is not an integer!")

    def test_invalid_input_float(self):
        self.assertEqual(amicable_numbers_sum(2.5), "Input is not an integer!")
