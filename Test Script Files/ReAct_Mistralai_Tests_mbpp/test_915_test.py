import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_zero(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_single_positive(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_single_negative(self):
        self.assertEqual(rearrange_numbs([-1]), [-1])

    def test_positive_and_zero(self):
        self.assertEqual(rearrange_numbs([1, 0]), [0, 1])

    def test_negative_and_zero(self):
        self.assertEqual(rearrange_numbs([-1, 0]), [0, -1])

    def test_mixed_positive_and_negative(self):
        self.assertEqual(rearrange_numbs([1, -2, 3, -4, 5]), [-4, -2, 1, 3, 5])

    def test_large_numbers(self):
        self.assertEqual(rearrange_numbs([1000000001, -1000000001, 0]), [0, -1000000001, 1000000001])

    def test_large_numbers_mixed(self):
        self.assertEqual(rearrange_numbs([1000000001, -1000000001, 0, 1, -2, 3, -4, 5]), [-4, -2, 0, 1, 3, -1000000001, 1000000001])

    def test_large_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1000000001, -1000000002]), [-1000000001, -1000000002])
