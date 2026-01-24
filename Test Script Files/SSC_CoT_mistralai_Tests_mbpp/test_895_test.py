import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5]), 10)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_sum_subseq([0, 0, 0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(max_sum_subseq([]), 0)
        self.assertEqual(max_sum_subseq([1]), 1)
        self.assertEqual(max_sum_subseq([-1]), -1)

    def test_boundary_cases(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4, 5, 6]), 16)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5, -6]), -12)
        self.assertEqual(max_sum_subseq([0, 0, 0, 0, 0, 0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4, -5]), 5)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, 5]), 5)
        self.assertEqual(max_sum_subseq([-1, -2, -3, 4, 5]), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_subseq(1.5)
        with self.assertRaises(TypeError):
            max_sum_subseq([1, 2, 3, "x", 5])
