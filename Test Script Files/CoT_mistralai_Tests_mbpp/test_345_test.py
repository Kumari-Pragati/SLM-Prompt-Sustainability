import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], diff_consecutivenums([]))

    def test_single_element_list(self):
        self.assertListEqual([None], diff_consecutivenums([1]))

    def test_consecutive_numbers(self):
        self.assertListEqual([1, 2, 3], diff_consecutivenums([1, 2, 3]))

    def test_negative_numbers(self):
        self.assertListEqual([1, -2, 3], diff_consecutivenums([1, -2, 3]))

    def test_zero_in_middle(self):
        self.assertListEqual([1, 0, 2], diff_consecutivenums([1, 0, 2]))

    def test_duplicate_numbers(self):
        self.assertListEqual([1, 1, 2], diff_consecutivenums([1, 1, 2]))

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, diff_consecutivenums, ['a', 'b', 'c'])
