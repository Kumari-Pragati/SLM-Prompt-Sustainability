import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 2), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)

    def test_boundary_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 2), 1)

    def test_edge_case(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 2), 0)

    def test_large_k(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 100), 10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated([1, 2, 3, 4], -4, 2)
        with self.assertRaises(ValueError):
            max_sub_array_sum_repeated([1, 2, 3, 4], 4, -2)
