import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_three_smallest_nums([-1, 0, 1, 2, 3]), 1)
        self.assertEqual(sum_three_smallest_nums([5, -1, 0, 2, 3]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_three_smallest_nums([0]), 0)
        self.assertEqual(sum_three_smallest_nums([1]), 1)
        self.assertEqual(sum_three_smallest_nums([-1]), 0)

    def test_edge_case_two_elements(self):
        self.assertEqual(sum_three_smallest_nums([0, 0]), 0)
        self.assertEqual(sum_three_smallest_nums([1, 0]), 1)
        self.assertEqual(sum_three_smallest_nums([0, 1]), 1)
        self.assertEqual(sum_three_smallest_nums([-1, 0]), 0)
        self.assertEqual(sum_three_smallest_nums([0, -1]), 0)

    def test_corner_case_all_negative(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), -3)
        self.assertEqual(sum_three_smallest_nums([-5, -4, -3, -2, -1]), -6)
