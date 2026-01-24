import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_element_array(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_multiple_elements_array(self):
        self.assertEqual(rearrange_numbs([1, 2, 3]), [1, 2, 3])

    def test_array_with_zero(self):
        self.assertEqual(rearrange_numbs([0, 1, 2]), [0, 2, 1])

    def test_array_with_negative_numbers(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3]), [-3, -2, -1])

    def test_array_with_positive_and_negative_numbers(self):
        self.assertEqual(rearrange_numbs([1, -2, 3, -4]), [1, -4, 3, -2])

    def test_array_with_duplicates(self):
        self.assertEqual(rearrange_numbs([1, 2, 2, 3, 3, 3]), [1, 3, 3, 2, 3, 2])
