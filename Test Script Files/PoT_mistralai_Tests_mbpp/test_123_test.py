import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(amicable_numbers_sum(28), 220)
        self.assertEqual(amicable_numbers_sum(100), 17296)
        self.assertEqual(amicable_numbers_sum(1000), 8382380)

    def test_invalid_input(self):
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(1.5), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum("str"), "Input is not an integer!")
