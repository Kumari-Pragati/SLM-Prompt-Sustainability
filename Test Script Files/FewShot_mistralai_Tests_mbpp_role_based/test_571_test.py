import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 1), 5)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 2), 7)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 3), 9)

    def test_empty_list(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 0), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([-1, -2, -3, -4], 4, 1), -5)
        self.assertEqual(max_sum_pair_diff_lessthan_K([-1, -2, -3, -4], 4, 2), -7)
        self.assertEqual(max_sum_pair_diff_lessthan_K([-1, -2, -3, -4], 4, 3), -9)

    def test_zero(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([0, 0], 2, 0), 0)

    def test_invalid_input_arr(self):
        with self.assertRaises(TypeError):
            max_sum_pair_diff_lessthan_K(1.5, 2, 3)

    def test_invalid_input_N(self):
        with self.assertRaises(TypeError):
            max_sum_pair_diff_lessthan_K([1, 2, 3], 'a', 3)

    def test_invalid_input_K(self):
        with self.assertRaises(TypeError):
            max_sum_pair_diff_lessthan_K([1, 2, 3], 2, 'a')
