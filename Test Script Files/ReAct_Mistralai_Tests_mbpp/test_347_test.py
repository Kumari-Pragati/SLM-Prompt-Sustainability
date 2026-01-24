import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(count_Squares(3, 4), 18)
        self.assertEqual(count_Squares(4, 4), 10)
        self.assertEqual(count_Squares(5, 5), 25)

    def test_zero_and_one(self):
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(count_Squares(-1, 0), 0)
        self.assertEqual(count_Squares(0, -1), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 1), 2)
        self.assertEqual(count_Squares(1, 2), 6)

    def test_large_numbers(self):
        self.assertEqual(count_Squares(100, 100), 338350)
        self.assertEqual(count_Squares(100, 101), 338350)
        self.assertEqual(count_Squares(101, 100), 338350)

    def test_invalid_input(self):
        self.assertRaises(ValueError, count_Squares, -1, 0)
        self.assertRaises(ValueError, count_Squares, 0, -1)
        self.assertRaises(ValueError, count_Squares, 0, 0)
