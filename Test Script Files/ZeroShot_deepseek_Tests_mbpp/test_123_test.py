import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_input_not_integer(self):
        self.assertEqual(amicable_numbers_sum("string"), "Input is not an integer!")

    def test_input_less_than_1(self):
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_amicable_numbers_sum(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)
        self.assertEqual(amicable_numbers_sum(285), 504)
        self.assertEqual(amicable_numbers_sum(100), 504)
