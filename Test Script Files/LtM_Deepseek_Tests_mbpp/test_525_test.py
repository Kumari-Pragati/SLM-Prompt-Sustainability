import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(parallel_lines((1, 2), (2, 4)))

    def test_edge_case_vertical_lines(self):
        self.assertFalse(parallel_lines((0, 1), (0, 2)))

    def test_edge_case_horizontal_lines(self):
        self.assertTrue(parallel_lines((1, 0), (2, 0)))

    def test_boundary_case_negative_coefficients(self):
        self.assertTrue(parallel_lines((-1, -2), (-2, -4)))

    def test_complex_case_non_integer_coefficients(self):
        self.assertTrue(parallel_lines((1.5, 2.5), (3, 5)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            parallel_lines((1, 2), (2, '4'))
