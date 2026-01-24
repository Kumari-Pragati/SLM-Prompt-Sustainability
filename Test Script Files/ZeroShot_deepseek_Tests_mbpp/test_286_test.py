import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_max_sub_array_sum_repeated(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 2), 10)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4], 4, 2), 3)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 4, 1), 10)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 1), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4], 4, 1), 3)
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
