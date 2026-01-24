import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(round_and_sum([1.5]), 1.5)

    def test_multiple_elements_list(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5]), 7.5)

    def test_list_with_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.5, -2.5, -3.5]), -7.5)

    def test_list_with_decimal_points(self):
        self.assertEqual(round_and_sum([1.25, 2.75, 3.25]), 7.25)

    def test_list_with_large_numbers(self):
        self.assertEqual(round_and_sum([100.5, 200.5, 300.5]), 601.5)
