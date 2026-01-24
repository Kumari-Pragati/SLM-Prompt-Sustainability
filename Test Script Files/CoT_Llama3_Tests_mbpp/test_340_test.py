import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, sum_three_smallest_nums, [-1, -2, -3, -4, -5])

    def test_mixed_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, -3, 4, 5]), 8)

    def test_empty_list(self):
        self.assertRaises(ValueError, sum_three_smallest_nums, [])

    def test_single_element_list(self):
        self.assertRaises(ValueError, sum_three_smallest_nums, [1])

    def test_list_with_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 2, 3, 3, 4]), 6)

    def test_list_with_duplicates_and_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 2, -3, -3, 4]), 6)
