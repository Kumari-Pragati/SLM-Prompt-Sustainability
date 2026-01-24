import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_zero(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_zero_and_negative_numbers(self):
        self.assertEqual(rearrange_numbs([0, -1, -2, -3, -4]), [0, -4, -3, -2, -1])

    def test_zero_and_positive_numbers(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_empty_array(self):
        self.assertEqual(rearrange_numbs([]), [])
