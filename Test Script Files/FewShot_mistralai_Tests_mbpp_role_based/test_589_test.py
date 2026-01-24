import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_perfect_square_in_range(self):
        self.assertEqual(perfect_squares(1, 16), [1, 4, 9, 16])

    def test_empty_range(self):
        self.assertEqual(perfect_squares(21, 21), [])

    def test_perfect_square_at_boundary(self):
        self.assertEqual(perfect_squares(1, 2), [])
        self.assertEqual(perfect_squares(2, 4), [4])
        self.assertEqual(perfect_squares(3, 9), [3, 9])
        self.assertEqual(perfect_squares(10, 14), [100])

    def test_non_perfect_square(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(16, 25), [16, 25])
        self.assertEqual(perfect_squares(26, 36), [])
