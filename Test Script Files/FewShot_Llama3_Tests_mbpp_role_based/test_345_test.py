import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [-1, 1, 1])

    def test_mixed_numbers(self):
        self.assertEqual(diff_consecutivenums([1, -2, 3, -4, 5]), [3, -1, 1])

    def test_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_list_with_one_element(self):
        self.assertEqual(diff_consecutivenums([1]), [])
