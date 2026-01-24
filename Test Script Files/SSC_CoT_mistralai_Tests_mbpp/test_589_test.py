import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_perfect_squares_typical_input(self):
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9, 16])

    def test_perfect_squares_edge_cases(self):
        self.assertListEqual(perfect_squares(1, 0), [])
        self.assertListEqual(perfect_squares(1, 1), [1])
        self.assertListEqual(perfect_squares(1, 2), [])
        self.assertListEqual(perfect_squares(100, 100), [100])
        self.assertListEqual(perfect_squares(100, 101), [])

    def test_perfect_squares_boundary_cases(self):
        self.assertListEqual(perfect_squares(0, 1), [])
        self.assertListEqual(perfect_squares(0, 4), [])
        self.assertListEqual(perfect_squares(1, 0), [])
        self.assertListEqual(perfect_squares(1, 1), [1])
        self.assertListEqual(perfect_squares(1, 2), [1])
        self.assertListEqual(perfect_squares(100, 100), [100])
        self.assertListEqual(perfect_squares(100, 101), [])
        self.assertListEqual(perfect_squares(101, 100), [])
        self.assertListEqual(perfect_squares(101, 101), [])

    def test_perfect_squares_invalid_input(self):
        self.assertRaises(TypeError, perfect_squares, 'a', 1)
        self.assertRaises(TypeError, perfect_squares, 1, 'b')
