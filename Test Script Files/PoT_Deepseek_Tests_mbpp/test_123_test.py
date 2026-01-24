import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(284), 504)

    def test_boundary_conditions(self):
        self.assertEqual(amicable_numbers_sum(1), 0)
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_edge_cases(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(-10), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum("string"), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(None), "Input is not an integer!")
