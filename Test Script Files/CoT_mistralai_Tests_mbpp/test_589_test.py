import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_empty_range(self):
        self.assertListEqual(perfect_squares(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(perfect_squares(4, 4), [4])

    def test_perfect_squares_in_range(self):
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9, 16])

    def test_no_perfect_squares_in_range(self):
        self.assertListEqual(perfect_squares(10, 20), [])

    def test_boundary_conditions(self):
        self.assertListEqual(perfect_squares(0, 1), [])
        self.assertListEqual(perfect_squares(1, 0), [])
        self.assertListEqual(perfect_squares(1, 1), [1])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, perfect_squares, 'a', 1)
        self.assertRaises(TypeError, perfect_squares, 1, 'b')
