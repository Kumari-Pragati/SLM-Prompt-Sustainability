import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(amicable_numbers_sum(300), 504)

    def test_boundary_conditions(self):
        self.assertEqual(amicable_numbers_sum(1), 0)
        self.assertEqual(amicable_numbers_sum(220), 284)

    def test_invalid_inputs(self):
        self.assertEqual(amicable_numbers_sum("100"), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(-10), "Input must be bigger than 0!")
