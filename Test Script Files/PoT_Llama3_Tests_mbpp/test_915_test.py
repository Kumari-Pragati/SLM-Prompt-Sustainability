import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_zero_in_middle(self):
        self.assertEqual(rearrange_numbs([1, 0, 3, 4, 5]), [1, 5, 0, 3, 4])

    def test_zero_at_start(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 4, 1, 2, 3])

    def test_zero_at_end(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 0]), [1, 2, 3, 4, 0])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, 3, 4, 5]), [-2, -1, 5, 4, 3])

    def test_all_positive_numbers(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])
