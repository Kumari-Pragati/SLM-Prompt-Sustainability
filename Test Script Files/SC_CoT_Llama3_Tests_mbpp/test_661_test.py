import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case_n_1(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)

    def test_edge_case_n_2(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_edge_case_n_3(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 5)

    def test_edge_case_n_4(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 6)

    def test_edge_case_n_5(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 9)

    def test_edge_case_n_6(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), 11)

    def test_invalid_input_n_zero(self):
        with self.assertRaises(IndexError):
            max_sum_of_three_consecutive([], 0)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(IndexError):
            max_sum_of_three_consecutive([1, 2, 3], -1)
