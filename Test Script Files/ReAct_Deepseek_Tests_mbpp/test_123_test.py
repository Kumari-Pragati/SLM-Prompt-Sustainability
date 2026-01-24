import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(284), 504)

    def test_small_number(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_large_number(self):
        self.assertEqual(amicable_numbers_sum(3000), 499417)

    def test_input_not_integer(self):
        self.assertEqual(amicable_numbers_sum("284"), "Input is not an integer!")

    def test_input_less_than_1(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_input_less_than_2(self):
        self.assertEqual(amicable_numbers_sum(1), 0)
