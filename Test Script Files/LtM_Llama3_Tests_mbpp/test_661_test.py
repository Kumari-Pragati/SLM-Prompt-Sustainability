import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 9)

    def test_edge_case1(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 5)

    def test_edge_case2(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_edge_case3(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_edge_case4(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)

    def test_edge_case5(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case6(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), 11)

    def test_edge_case7(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7], 7), 12)

    def test_edge_case8(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8], 8), 13)

    def test_edge_case9(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 14)

    def test_edge_case10(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 15)
