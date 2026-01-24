import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(amicable_numbers_sum(10000), 31626)

    def test_invalid_input_type(self):
        self.assertEqual(amicable_numbers_sum("abc"), "Input is not an integer!")

    def test_invalid_input_value(self):
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")

    def test_edge_case(self):
        self.assertEqual(amicable_numbers_sum(1), 0)

    def test_edge_case2(self):
        self.assertEqual(amicable_numbers_sum(2), 2)

    def test_edge_case3(self):
        self.assertEqual(amicable_numbers_sum(3), 3)
