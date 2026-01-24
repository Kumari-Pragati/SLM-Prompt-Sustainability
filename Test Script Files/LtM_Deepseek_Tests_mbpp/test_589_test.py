import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(20, 30), [25])

    def test_edge_conditions(self):
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(100, 100), [])
        self.assertEqual(perfect_squares(0, 100), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_boundary_conditions(self):
        self.assertEqual(perfect_squares(10000, 10100), [10201])
        self.assertEqual(perfect_squares(31415, 31515), [31524])

    def test_complex_cases(self):
        self.assertEqual(perfect_squares(100000, 100100), [100404, 100804])
        self.assertEqual(perfect_squares(99999, 100099), [100000])
