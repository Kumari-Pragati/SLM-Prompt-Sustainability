import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])
        self.assertListEqual(diff_consecutivenums([0, 1, 2, 3, 4]), [0, 1, 1])
        self.assertListEqual(diff_consecutivenums([-1, 0, 1, 2, 3]), [-1, 1, 1, 1])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(diff_consecutivenums([1]), [None])
        self.assertListEqual(diff_consecutivenums([1, 2]), [1])
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5, 6]), [1, 1, 1])
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5, 6, 7]), [1, 1, 1, 1])
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5, 6, 7, 8]), [1, 1, 1, 1, 1])

    def test_negative_numbers(self):
        self.assertListEqual(diff_consecutivenums([-1, -2, -3, -4]), [1, 3, 5])
        self.assertListEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [1, 3, 5, 7])

    def test_invalid_input(self):
        self.assertRaises(TypeError, diff_consecutivenums, [1, 2, 3, "a", 5])
        self.assertRaises(TypeError, diff_consecutivenums, [1, 2, 3, 4, "a"])
