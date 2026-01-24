import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([-2,1,-3,4,-1,2,1,-5,4], 9), 6)

    def test_edge_case_start(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4,5], 5), 5)

    def test_edge_case_end(self):
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5], 5), 1)

    def test_edge_case_zero(self):
        self.assertEqual(max_sub_array_sum([0,0,0,0,0], 5), 1)

    def test_edge_case_single(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_edge_case_empty(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(max_sub_array_sum([-1,-2,-3,-4,-5], 5), 1)

    def test_edge_case_positive(self):
        self.assertEqual(max_sub_array_sum([1,2,3,4,5], 5), 5)

    def test_edge_case_mixed(self):
        self.assertEqual(max_sub_array_sum([-1,2,-3,4,-1,2,1,-5,4], 9), 6)
