import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_two_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_three_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)

    def test_four_elements_list(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4], 4), -6)

    def test_large_numbers(self):
        self.assertEqual(max_sum_of_three_consecutive([1000000001, 1000000002, 1000000003, 1000000004], 4), 3000000006)
