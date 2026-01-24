import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_positive_num(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_single_negative_num(self):
        self.assertEqual(sum_three_smallest_nums([-1]), 0)

    def test_single_zero(self):
        self.assertEqual(sum_three_smallest_nums([0]), 0)

    def test_three_positive_nums(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)

    def test_three_negative_nums(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), -6)

    def test_three_mixed_nums(self):
        self.assertEqual(sum_three_smallest_nums([1, -2, 3]), 2)

    def test_list_with_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([1, 1, 2, 3]), 6)

    def test_list_with_negative_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([-1, -1, -2, -3]), -6)

    def test_list_with_zero(self):
        self.assertEqual(sum_three_smallest_nums([0, 1, 2]), 3)

    def test_list_with_zero_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([0, 0, 1, 2]), 3)
