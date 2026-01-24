import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_three_smallest_nums([5, 2, 1, 4, 3]), 6)
        self.assertEqual(sum_three_smallest_nums([-1, 0, 1, 2, 3]), 3)

    def test_edge_cases(self):
        self.assertEqual(sum_three_smallest_nums([0, 0, 0]), 0)
        self.assertEqual(sum_three_smallest_nums([1, 0, 0]), 1)
        self.assertEqual(sum_three_smallest_nums([0, 1, 0]), 1)
        self.assertEqual(sum_three_smallest_nums([0, 0, 1]), 1)
        self.assertEqual(sum_three_smallest_nums([0, 1, 1]), 1)
        self.assertEqual(sum_three_smallest_nums([1, 1, 1]), 3)

    def test_boundary_conditions(self):
        self.assertEqual(sum_three_smallest_nums([-10, -9, -8, 0, 1]), -8)
        self.assertEqual(sum_three_smallest_nums([1000000000, 1, 0, -1, -2]), 1)
        self.assertEqual(sum_three_smallest_nums([-1000000000, -1, 0, 1, 10]), -1)
