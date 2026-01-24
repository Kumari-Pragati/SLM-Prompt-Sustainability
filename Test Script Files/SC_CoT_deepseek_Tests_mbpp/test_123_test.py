import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_boundary_case(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_edge_case(self):
        self.assertEqual(amicable_numbers_sum(220), 284)
        self.assertEqual(amicable_numbers_sum(284), 220)

    def test_invalid_input(self):
        self.assertEqual(amicable_numbers_sum("10000"), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(-10000), "Input must be bigger than 0!")
