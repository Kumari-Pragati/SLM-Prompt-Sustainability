import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_zero(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_positive_numbers(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4]), [-1, -4, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(rearrange_numbs([0, 1, -2, 3, -4, 2]), [0, 1, -4, -2, 3, 2])

    def test_zero_and_negative_numbers(self):
        self.assertEqual(rearrange_numbs([0, -1]), [-1, 0])

    def test_zero_and_positive_numbers(self):
        self.assertEqual(rearrange_numbs([0, 1]), [0, 1])

    def test_zero_and_mixed_numbers(self):
        self.assertEqual(rearrange_numbs([0, -1, 1]), [-1, 0, 1])

    def test_large_numbers(self):
        self.assertEqual(rearrange_numbs([1e10, 2e10, 3e10, 4e10]), [1e10, 4e10, 2e10, 3e10])

    def test_small_numbers(self):
        self.assertEqual(rearrange_numbs([1e-10, 2e-10, 3e-10, 4e-10]), [1e-10, 4e-10, 2e-10, 3e-10])
