import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_edge_case_zero(self):
        self.assertEqual(sum_three_smallest_nums([0, 0, 0, 0, 0]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, -4, -5]), 0)

    def test_edge_case_single_positive(self):
        self.assertEqual(sum_three_smallest_nums([1]), 1)

    def test_edge_case_single_negative(self):
        self.assertEqual(sum_three_smallest_nums([-1]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, -4, -5]), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(sum_three_smallest_nums([1, -2, 3, -4, 5]), 6)
