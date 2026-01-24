import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_diff_consecutivenums_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_diff_consecutivenums_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_diff_consecutivenums_two_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2]), [1])

    def test_diff_consecutivenums_three_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3]), [1, 1])

    def test_diff_consecutivenums_four_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1, 1])

    def test_diff_consecutivenums_five_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1, 1])

    def test_diff_consecutivenums_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [1, 1, 1, 1])

    def test_diff_consecutivenums_positive_and_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([1, -2, 3, -4, 5]), [3, -7, 9, -1])
