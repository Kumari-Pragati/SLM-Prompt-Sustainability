import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(rearrange_numbs([]), [])

    def test_single_zero(self):
        self.assertListEqual(rearrange_numbs([0]), [0])

    def test_single_positive(self):
        self.assertListEqual(rearrange_numbs([1]), [1])

    def test_single_negative(self):
        self.assertListEqual(rearrange_numbs([-1]), [-1])

    def test_mixed_numbers(self):
        self.assertListEqual(rearrange_numbs([0, 1, -1, 2, -2, 3, -3, 4, -4]), [0, 1, -1, -2, 2, -3, 3, -4, 4])

    def test_large_numbers(self):
        self.assertListEqual(rearrange_numbs([1000000000, -1000000000, 1, -1, 0]), [0, 1, -1, -1000000000, 1000000000])
