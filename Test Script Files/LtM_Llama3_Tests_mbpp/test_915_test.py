import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNumbs(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(rearrange_numbs([]), [])

    def test_single_element_input(self):
        self.assertEqual(rearrange_numbs([1]), [1])

    def test_single_zero_input(self):
        self.assertEqual(rearrange_numbs([0]), [0])

    def test_multiple_elements_input(self):
        self.assertEqual(rearrange_numbs([1, 2, 3]), [1, 2, 3])

    def test_negative_elements_input(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3]), [-3, -2, -1])

    def test_zero_and_negative_elements_input(self):
        self.assertEqual(rearrange_numbs([0, -1, -2, -3]), [0, -3, -2, -1])

    def test_zero_and_positive_elements_input(self):
        self.assertEqual(rearrange_numbs([0, 1, 2, 3]), [0, 3, 2, 1])

    def test_all_positive_elements_input(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_all_negative_elements_input(self):
        self.assertEqual(rearrange_numbs([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

    def test_mixed_elements_input(self):
        self.assertEqual(rearrange_numbs([1, -2, 3, 0, -4]), [4, 3, 1, 0, -2])
