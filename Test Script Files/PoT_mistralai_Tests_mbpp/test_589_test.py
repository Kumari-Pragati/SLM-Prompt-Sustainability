import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9, 16])
        self.assertListEqual(perfect_squares(25, 36), [4, 9, 16, 25])
        self.assertListEqual(perfect_squares(49, 64), [7, 9, 16, 25, 36, 49])

    def test_edge_cases(self):
        self.assertListEqual(perfect_squares(0, 1), [])
        self.assertListEqual(perfect_squares(1, 0), [])
        self.assertListEqual(perfect_squares(1, 1), [1])
        self.assertListEqual(perfect_squares(16, 16), [16])

    def test_boundary_cases(self):
        self.assertListEqual(perfect_squares(1, 2), [])
        self.assertListEqual(perfect_squares(2, 1), [1])
        self.assertListEqual(perfect_squares(16, 15), [4, 9])
        self.assertListEqual(perfect_squares(15, 16), [1, 4, 9])
