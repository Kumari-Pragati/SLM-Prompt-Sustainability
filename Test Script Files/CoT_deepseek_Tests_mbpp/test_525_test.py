import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(parallel_lines((1, 2), (2, 4)))

    def test_typical_case_2(self):
        self.assertFalse(parallel_lines((1, 2), (3, 4)))

    def test_vertical_lines(self):
        self.assertTrue(parallel_lines((0, 2), (0, 4)))

    def test_horizontal_lines(self):
        self.assertFalse(parallel_lines((1, 0), (3, 0)))

    def test_same_line(self):
        self.assertTrue(parallel_lines((1, 2), (1, 2)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallel_lines((1, 2), (2,))
