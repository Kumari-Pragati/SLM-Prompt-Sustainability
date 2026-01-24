import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(parallel_lines([1, 2], [3, 4]))

    def test_parallel_lines(self):
        self.assertTrue(parallel_lines([1, 1], [2, 2]))

    def test_non_parallel_lines(self):
        self.assertFalse(parallel_lines([1, 2], [3, 5]))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            parallel_lines([0, 1], [1, 1])

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            parallel_lines([], [1, 1])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            parallel_lines('abc', [1, 1])
