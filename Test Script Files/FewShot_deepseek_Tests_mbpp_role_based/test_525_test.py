import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(parallel_lines((1, 2), (2, 4)))

    def test_edge_case(self):
        self.assertTrue(parallel_lines((0, 1), (0, 2)))

    def test_boundary_case(self):
        self.assertFalse(parallel_lines((1, 0), (2, 0)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallel_lines((1, 2), (2, 'a'))
