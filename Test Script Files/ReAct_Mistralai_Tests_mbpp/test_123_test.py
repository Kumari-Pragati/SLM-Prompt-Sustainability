import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(amicable_numbers_sum(28), 220)
        self.assertEqual(amicable_numbers_sum(220), 28)
        self.assertEqual(amicable_numbers_sum(221), 0)  # No amicable pairs below 221
        self.assertEqual(amicable_numbers_sum(1000), 31626)

    def test_invalid_input(self):
        self.assertEqual(amicable_numbers_sum('not_an_integer'), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
