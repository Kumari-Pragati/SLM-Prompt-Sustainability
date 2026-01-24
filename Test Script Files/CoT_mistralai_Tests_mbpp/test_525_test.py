import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_parallel_lines_positive(self):
        self.assertTrue(parallel_lines((1, 2), (3, 6)))
        self.assertTrue(parallel_lines((-1, 2), (3, 6)))
        self.assertTrue(parallel_lines((1, -2), (3, -6)))
        self.assertTrue(parallel_lines((-1, -2), (-3, -6)))

    def test_parallel_lines_zero_slope(self):
        self.assertTrue(parallel_lines((0, 1), (0, 1)))
        self.assertTrue(parallel_lines((0, -1), (0, -1)))

    def test_parallel_lines_negative(self):
        self.assertFalse(parallel_lines((1, 2), (3, 4)))
        self.assertFalse(parallel_lines((-1, 2), (3, 4)))
        self.assertFalse(parallel_lines((1, -2), (3, -4)))
        self.assertFalse(parallel_lines((-1, -2), (-3, -4)))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, parallel_lines, (0, 0))
        self.assertRaises(ValueError, parallel_lines, (0, None))
        self.assertRaises(ValueError, parallel_lines, (None, 0))
        self.assertRaises(ValueError, parallel_lines, (None, None))
