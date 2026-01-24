import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_element_array(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_zero_in_array(self):
        self.assertEqual(rearrange_numbs([0, 1, 2]), [0, 2, 1])

    def test_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, 0, 1, 2]), [-2, -1, 0, 2, 1])

    def test_positive_numbers(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_numbers(self):
        self.assertEqual(rearrange_numbs([0, -1, 2, -3, 4]), [0, -3, -1, 2, 4])
