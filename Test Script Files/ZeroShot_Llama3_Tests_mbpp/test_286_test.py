import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_max_sub_array_sum_repeated(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 5, 2), 5)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5, 6], 6, 3), 9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5, -6], 6, 3), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5, -6], 6, 3), 5)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5, -6], 6, 3), -1)
