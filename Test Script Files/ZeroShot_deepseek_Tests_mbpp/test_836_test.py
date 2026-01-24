import unittest
from mbpp_836_code import maxsize
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_max_sub_array_sum(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)
        self.assertEqual(max_sub_array_sum([1, 2, 3, -4, 5, -6, 7, 8], 8), 8)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5, -6, -7, -8], 8), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8], 8), 8)
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4, 5, -6, 7, -8], 8), 8)
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, -5, 6, -7, 8], 8), 8)
