import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines(self):
        # Test case where lines are parallel
        self.assertTrue(parallel_lines((1, 2), (2, 4)))
        self.assertTrue(parallel_lines((3, 6), (6, 12)))
        self.assertTrue(parallel_lines((-1, 2), (2, -4)))

        # Test case where lines are not parallel
        self.assertFalse(parallel_lines((1, 2), (3, 6)))
        self.assertFalse(parallel_lines((3, 6), (9, 18)))
        self.assertFalse(parallel_lines((-1, 2), (1, -2)))

        # Test case where denominator is zero
        with self.assertRaises(ZeroDivisionError):
            parallel_lines((1, 0), (2, 0))

        # Test case where numerator is zero
        self.assertTrue(parallel_lines((0, 2), (0, 4)))
