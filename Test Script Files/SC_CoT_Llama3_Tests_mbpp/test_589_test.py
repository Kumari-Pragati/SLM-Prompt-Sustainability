import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        self.assertEqual(perfect_squares(5, 20), [5, 6, 7, 8, 9, 10, 12, 13, 16, 18, 19])

    def test_edge_cases(self):
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(1, 2), [1])
        self.assertEqual(perfect_squares(2, 2), [1, 4])

    def test_boundary_cases(self):
        self.assertEqual(perfect_squares(1, 3), [1])
        self.assertEqual(perfect_squares(1, 4), [1])
        self.assertEqual(perfect_squares(2, 4), [1, 4])

    def test_special_cases(self):
        self.assertEqual(perfect_squares(1, 5), [1, 4])
        self.assertEqual(perfect_squares(5, 5), [5])
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perfect_squares('a', 10)
        with self.assertRaises(TypeError):
            perfect_squares(1, 'b')
