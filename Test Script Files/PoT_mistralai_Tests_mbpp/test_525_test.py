import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_parallel_lines_typical(self):
        self.assertTrue(parallel_lines((1, 2), (3, 6)))
        self.assertTrue(parallel_lines((-1, 2), (3, 6)))
        self.assertTrue(parallel_lines((1, -2), (3, -6)))
        self.assertTrue(parallel_lines((-1, -2), (-3, -6)))

    def test_parallel_lines_edge(self):
        self.assertFalse(parallel_lines((0, 2), (3, 6)))
        self.assertFalse(parallel_lines((1, 0), (3, 6)))
        self.assertFalse(parallel_lines((1, 2), (0, 6)))
        self.assertFalse(parallel_lines((1, 2), (3, 0)))
