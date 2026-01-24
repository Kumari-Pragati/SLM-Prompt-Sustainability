import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(sum_three_smallest_nums([5]), 5)

    def test_two_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([3, 5]), 8)

    def test_three_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 15)

    def test_four_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6]), 15)

    def test_more_than_three_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6, 7]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, 3]), 3)

    def test_zero(self):
        self.assertEqual(sum_three_smallest_nums([0, 1, 2]), 3)

    def test_floats(self):
        self.assertEqual(sum_three_smallest_nums([1.1, 2.2, 3.3]), 6.6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, 0, 1, 2, 3]), 6)
