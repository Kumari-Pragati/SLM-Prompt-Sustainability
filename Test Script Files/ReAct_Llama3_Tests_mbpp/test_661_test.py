import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_three_elements(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)

    def test_four_elements(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 9)

    def test_five_elements(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 12)

    def test_edge_case(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3], 3), -1)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4], 4), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), 14)

    def test_all_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5, -6], 6), -1)
