import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(amicable_numbers_sum(220), 284)

    def test_boundary_conditions(self):
        self.assertEqual(amicable_numbers_sum(1), 0)
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum('a'), "Input is not an integer!")

    def test_complex_cases(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)
