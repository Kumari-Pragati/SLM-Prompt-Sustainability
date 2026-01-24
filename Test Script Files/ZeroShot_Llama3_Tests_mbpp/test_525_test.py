import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines(self):
        self.assertTrue(parallel_lines([(1, 2), (3, 4)], [(1, 2), (3, 4)]))
        self.assertFalse(parallel_lines([(1, 2), (3, 4)], [(1, 3), (3, 4)]))
        self.assertTrue(parallel_lines([(1, 2), (2, 3)], [(1, 2), (2, 3)]))
        self.assertFalse(parallel_lines([(1, 2), (2, 3)], [(1, 3), (2, 3)]))
        self.assertTrue(parallel_lines([(1, 2), (1, 2)], [(1, 2), (1, 2)]))
        self.assertFalse(parallel_lines([(1, 2), (1, 2)], [(1, 3), (1, 2)]))
        self.assertTrue(parallel_lines([(1, 2), (1, 2)], [(1, 2), (1, 2)]))
        self.assertFalse(parallel_lines([(1, 2), (1, 2)], [(1, 3), (1, 2)]))
