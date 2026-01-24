import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_max_sub_array_sum(self):
        self.assertEqual(max_sub_array_sum([-2,1,-3,4,-1,2,1,-5,4], 9), 6)
        self.assertEqual(max_sub_array_sum([1,2,3,4,5], 5), 15)
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5], 5), -1)
        self.assertEqual(max_sub_array_sum([1,2,3,4,5,6,7,8,9], 9), 27)
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5,-6,-7,-8,-9], 9, -1), -1)
        self.assertEqual(max_sub_array_sum([1,2,3,4,5,6,7,8,9], 0), 0)
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_max_sub_array_sum_edge_cases(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), -1)
        self.assertEqual(max_sub_array_sum([1,2], 2), 2)
        self.assertEqual(max_sub_array_sum([-1,-2], 2), -1)
