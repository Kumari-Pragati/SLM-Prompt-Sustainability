import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])
        self.assertEqual(diff_consecutivenums([5, 4, 3, 2, 1]), [-1, -1, -1, -1])

    def test_zero(self):
        self.assertEqual(diff_consecutivenums([0, 0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [1, 1, 1])
        self.assertEqual(diff_consecutivenums([-5, -4, -3, -2, -1]), [-1, -1, -1, -1])

    def test_empty_list(self):
        self.assertListEqual(diff_consecutivenums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(diff_consecutivenums([1]), [])

    def test_single_element_list_with_zero(self):
        self.assertListEqual(diff_consecutivenums([0]), [])
