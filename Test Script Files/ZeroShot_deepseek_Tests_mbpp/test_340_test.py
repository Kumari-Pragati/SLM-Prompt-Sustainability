import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_three_smallest_nums([10, 20, 30, 40, 50]), 60)

    def test_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(sum_three_smallest_nums([-10, -20, -30, -40, -50]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, 2, -3, 4, -5]), 5)
        self.assertEqual(sum_three_smallest_nums([-10, 20, -30, 40, -50]), 30)

    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_two_elements(self):
        self.assertEqual(sum_three_smallest_nums([1, 2]), 0)
