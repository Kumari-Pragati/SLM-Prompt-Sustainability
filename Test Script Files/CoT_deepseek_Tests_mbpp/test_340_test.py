import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_with_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 4, 5]), 4)

    def test_with_zero(self):
        self.assertEqual(sum_three_smallest_nums([0, 2, 3, 4, 5]), 9)

    def test_with_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([1, 1, 1, 4, 5]), 6)

    def test_with_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_with_single_element(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_with_two_elements(self):
        self.assertEqual(sum_three_smallest_nums([1, 2]), 0)

    def test_with_all_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), 0)

    def test_with_all_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)

    def test_with_large_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1000, 2000, 3000, 4000, 5000]), 6000)
