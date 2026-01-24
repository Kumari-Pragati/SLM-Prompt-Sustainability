import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(2, 2), [1, 4])
        self.assertEqual(perfect_squares(3, 3), [1, 4, 9])
        self.assertEqual(perfect_squares(4, 4), [1, 4, 9, 16])
        self.assertEqual(perfect_squares(5, 5), [1, 4, 9, 16, 25])

    def test_edge(self):
        self.assertEqual(perfect_squares(0, 0), [])
        self.assertEqual(perfect_squares(1, 1), [1])
        self.assertEqual(perfect_squares(2, 2), [1, 4])
        self.assertEqual(perfect_squares(3, 3), [1, 4, 9])
        self.assertEqual(perfect_squares(4, 4), [1, 4, 9, 16])
        self.assertEqual(perfect_squares(5, 5), [1, 4, 9, 16, 25])
        self.assertEqual(perfect_squares(6, 6), [1, 4, 9, 16, 25, 36])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            perfect_squares('a', 1)
        with self.assertRaises(TypeError):
            perfect_squares(1, 'b')
