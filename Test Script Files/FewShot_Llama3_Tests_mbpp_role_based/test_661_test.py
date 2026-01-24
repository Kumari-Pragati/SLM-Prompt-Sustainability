import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_two_element_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_three_element_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)

    def test_four_element_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 9)

    def test_five_element_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 12)

    def test_large_array(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 27)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 5), -6)

    def test_zero(self):
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0, 0, 0], 5), 0)
