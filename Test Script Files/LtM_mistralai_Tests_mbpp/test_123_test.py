import unittest
from mbpp_123_code import amicable_numbers_sum

class TestAmicableNumbersSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(amicable_numbers_sum(220), 284)
        self.assertEqual(amicable_numbers_sum(284), 220)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(amicable_numbers_sum(1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(0), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(-1), "Input must be bigger than 0!")
        self.assertEqual(amicable_numbers_sum(1024), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(1.0), "Input is not an integer!")
        self.assertEqual(amicable_numbers_sum(2), "Input must be bigger than 0!")

    def test_complex_and_corner_cases(self):
        self.assertEqual(amicable_numbers_sum(10), 12)
        self.assertEqual(amicable_numbers_sum(1000), 989)
        self.assertEqual(amicable_numbers_sum(10000), 9561)
        self.assertEqual(amicable_numbers_sum(100000), 95611)
