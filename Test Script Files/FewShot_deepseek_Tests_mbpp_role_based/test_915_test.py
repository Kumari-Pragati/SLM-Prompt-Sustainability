import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearrange_nums([3, 1, 2]), [1, 2, 3])

    def test_with_zero(self):
        self.assertEqual(rearrange_nums([0, 1, 2]), [0, 1, 2])

    def test_with_negative_numbers(self):
        self.assertEqual(rearrange_nums([-1, -2, -3]), [-1, -2, -3])

    def test_with_duplicates(self):
        self.assertEqual(rearrange_nums([3, 1, 2, 1]), [1, 1, 2, 3])

    def test_with_large_numbers(self):
        self.assertEqual(rearrange_nums([100, 200, 300]), [100, 200, 300])

    def test_with_empty_list(self):
        self.assertEqual(rearrange_nums([]), [])

    def test_with_single_element(self):
        self.assertEqual(rearrange_nums([1]), [1])

    def test_with_float_numbers(self):
        self.assertEqual(rearrange_nums([1.5, 2.5, 3.5]), [1.5, 2.5, 3.5])

    def test_with_negative_zero(self):
        self.assertEqual(rearrange_nums([0, -1, -2]), [0, -1, -2])
