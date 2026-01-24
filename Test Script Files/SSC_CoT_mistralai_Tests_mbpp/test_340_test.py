import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, -1, 0, 7, 8]), 6)
        self.assertEqual(sum_three_smallest_nums([-2, -1, 0, 1, 2]), -1)
        self.assertEqual(sum_three_smallest_nums([0, 0, 0, 1, 2, 3]), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_three_smallest_nums([-1000, -999, -1, 0, 1]), -1000)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6]), 15)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6, 7]), 16)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6, 7, 8]), 21)
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]), 24)

        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), -6)
        self.assertEqual(sum_three_smallest_nums([0, 0, 0]), 0)
        self.assertEqual(sum_three_smallest_nums([-1, 0, 1]), 0)
        self.assertEqual(sum_three_smallest_nums([-1, 0, 0, 1]), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum_three_smallest_nums, 123)
        self.assertRaises(TypeError, sum_three_smallest_nums, (1, 2, 3))
        self.assertRaises(TypeError, sum_three_smallest_nums, [1, 2, 3, 'a'])
