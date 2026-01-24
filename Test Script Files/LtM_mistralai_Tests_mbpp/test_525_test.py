import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_simple_parallel(self):
        self.assertTrue(parallel_lines([1, 2], [2, 4]))
        self.assertTrue(parallel_lines([-1, 2], [-2, 4]))
        self.assertTrue(parallel_lines([1, -2], [2, -4]))

    def test_zero_slope(self):
        self.assertTrue(parallel_lines([0, 1], [0, 1]))
        self.assertTrue(parallel_lines([0, -1], [0, -1]))

    def test_opposite_slope(self):
        self.assertFalse(parallel_lines([1, 2], [-1, -2]))
        self.assertFalse(parallel_lines([-1, 2], [1, -2]))
        self.assertFalse(parallel_lines([1, -2], [-1, 2]))

    def test_empty_input(self):
        self.assertRaises(ValueError, parallel_lines, (), ())
        self.assertRaises(ValueError, parallel_lines, (1, 0), ())
        self.assertRaises(ValueError, parallel_lines, (), (1, 0))
