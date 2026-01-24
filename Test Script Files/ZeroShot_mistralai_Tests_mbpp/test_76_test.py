import unittest
from76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_squares_valid_input(self):
        self.assertEqual(count_Squares(1, 2), 1)
        self.assertEqual(count_Squares(2, 3), 3)
        self.assertEqual(count_Squares(3, 4), 10)
        self.assertEqual(count_Squares(4, 5), 14)
        self.assertEqual(count_Squares(5, 6), 27)

    def test_count_squares_invalid_input(self):
        self.assertRaises(ValueError, count_Squares, -1, 2)
        self.assertRaises(ValueError, count_Squares, 1, -1)
        self.assertRaises(ValueError, count_Squares, 0, 0)
