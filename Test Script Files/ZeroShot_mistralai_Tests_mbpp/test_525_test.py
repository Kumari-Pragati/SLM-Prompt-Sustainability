import unittest
from mbpp_525_code import List

from 525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines_same_slope(self):
        self.assertTrue(parallel_lines([1, 2], [2, 4]))
        self.assertTrue(parallel_lines([-1, -2], [-2, -4]))
        self.assertTrue(parallel_lines([0, 1], [1, 0]))

    def test_parallel_lines_different_slope(self):
        self.assertFalse(parallel_lines([1, 2], [2, 3]))
        self.assertFalse(parallel_lines([-1, -2], [-3, -2]))
        self.assertFalse(parallel_lines([0, 1], [1, 2]))

    def test_parallel_lines_zero_slope(self):
        self.assertTrue(parallel_lines([0, 0], [0, 0]))
        self.assertRaises(ValueError, parallel_lines, [0, 0], [0, 1])
        self.assertRaises(ValueError, parallel_lines, [0, 1], [0, 0])

    def test_parallel_lines_invalid_input(self):
        self.assertRaises(TypeError, parallel_lines, 1, 2)
        self.assertRaises(TypeError, parallel_lines, [1], [2])
        self.assertRaises(TypeError, parallel_lines, [1, 2], "3")
