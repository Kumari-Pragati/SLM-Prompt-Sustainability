import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 4)
        self.assertEqual(count_Odd_Squares(16, 25), 3)
        self.assertEqual(count_Odd_Squares(26, 36), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(0, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 4), 0)
        self.assertEqual(count_Odd_Squares(25, 25), 0)

    def test_negative_and_non_integer_input(self):
        self.assertRaises(TypeError, count_Odd_Squares, -1, 4)
        self.assertRaises(TypeError, count_Odd_Squares, 1, -2)
        self.assertRaises(TypeError, count_Odd_Squares, 'a', 4)
        self.assertRaises(TypeError, count_Odd_Squares, 1, 2.5)
