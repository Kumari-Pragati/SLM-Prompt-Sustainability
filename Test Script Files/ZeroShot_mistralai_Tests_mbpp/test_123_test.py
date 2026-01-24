import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(amicable_numbers_sum("test"), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")

    def test_empty_set(self):
        self.assertEqual(amicable_numbers_sum(0), 0)

    def test_small_limit(self):
        self.assertEqual(amicable_numbers_sum(1), 0)
        self.assertEqual(amicable_numbers_sum(2), 0)
        self.assertEqual(amicable_numbers_sum(3), 0)
        self.assertEqual(amicable_numbers_sum(4), 220)

    def test_large_limit(self):
        self.assertEqual(amicable_numbers_sum(10), 985)
        self.assertEqual(amicable_numbers_sum(100), 61225)
        self.assertEqual(amicable_numbers_sum(1000), 316260320)
