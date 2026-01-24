import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], diff_consecutivenums([]))

    def test_single_element_list(self):
        self.assertListEqual([], diff_consecutivenums([1]))

    def test_two_elements_list(self):
        self.assertListEqual([1], diff_consecutivenums([1, 2]))

    def test_consecutive_increasing_numbers(self):
        self.assertListEqual([1, 2, 3, 4], diff_consecutivenums([1, 2, 3, 4, 5]))

    def test_consecutive_decreasing_numbers(self):
        self.assertListEqual([1, -1, -2], diff_consecutivenums([5, 4, 3]))

    def test_mixed_numbers(self):
        self.assertListEqual([2, -1, 3], diff_consecutivenums([1, 2, 3, -4, 5]))

    def test_negative_numbers(self):
        self.assertListEqual([-1, -1], diff_consecutivenums([-2, -1]))
