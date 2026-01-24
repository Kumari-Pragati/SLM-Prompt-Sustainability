import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_parallel_lines_with_valid_input(self):
        line1 = [1, 2]
        line2 = [2, 4]
        self.assertTrue(parallel_lines(line1, line2))

    def test_parallel_lines_with_non_parallel_lines(self):
        line1 = [1, 2]
        line2 = [3, 4]
        self.assertFalse(parallel_lines(line1, line2))

    def test_parallel_lines_with_zero_slope(self):
        line1 = [0, 1]
        line2 = [0, 2]
        self.assertTrue(parallel_lines(line1, line2))

    def test_parallel_lines_with_infinite_slope(self):
        line1 = [1, 0]
        line2 = [2, 0]
        self.assertTrue(parallel_lines(line1, line2))

    def test_parallel_lines_with_invalid_input_type(self):
        line1 = "string"
        line2 = [1, 2]
        with self.assertRaises(TypeError):
            parallel_lines(line1, line2)

    def test_parallel_lines_with_invalid_input_structure(self):
        line1 = [1, 2, 3]
        line2 = [1, 2]
        with self.assertRaises(TypeError):
            parallel_lines(line1, line2)
