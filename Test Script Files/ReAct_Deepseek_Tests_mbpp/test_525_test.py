import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(parallel_lines((1, 2), (2, 4)))

    def test_typical_case_2(self):
        self.assertTrue(parallel_lines((3, 6), (6, 12)))

    def test_edge_case_vertical_lines(self):
        self.assertFalse(parallel_lines((0, 1), (0, 2)))

    def test_edge_case_horizontal_lines(self):
        self.assertTrue(parallel_lines((1, 0), (2, 0)))

    def test_edge_case_same_slope(self):
        self.assertTrue(parallel_lines((1, 2), (1, 3)))

    def test_edge_case_different_slope(self):
        self.assertFalse(parallel_lines((1, 2), (2, 4)))

    def test_error_case_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            parallel_lines((1, 0), (2, 0))

    def test_error_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            parallel_lines((1, 'a'), (2, 4))
