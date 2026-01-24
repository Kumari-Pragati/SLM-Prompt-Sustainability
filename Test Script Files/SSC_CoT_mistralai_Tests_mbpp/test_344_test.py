import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Odd_Squares(1, 36), 5)
        self.assertEqual(count_Odd_Squares(10, 121), 13)
        self.assertEqual(count_Odd_Squares(100, 225), 21)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(0, 4), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(4, 9), 1)
        self.assertEqual(count_Odd_Squares(25, 25), 0)
        self.assertEqual(count_Odd_Squares(26, 25), 0)
        self.assertEqual(count_Odd_Squares(27, 25), 0)
        self.assertEqual(count_Odd_Squares(28, 25), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 2), 0)
        self.assertEqual(count_Odd_Squares(2, 2), 0)
        self.assertEqual(count_Odd_Squares(3, 2), 0)
        self.assertEqual(count_Odd_Squares(4, 2), 1)
        self.assertEqual(count_Odd_Squares(5, 2), 0)

        self.assertEqual(count_Odd_Squares(1, 3), 0)
        self.assertEqual(count_Odd_Squares(2, 3), 0)
        self.assertEqual(count_Odd_Squares(3, 3), 0)
        self.assertEqual(count_Odd_Squares(4, 3), 1)
        self.assertEqual(count_Odd_Squares(5, 3), 0)

        self.assertEqual(count_Odd_Squares(1, 4), 0)
        self.assertEqual(count_Odd_Squares(2, 4), 0)
        self.assertEqual(count_Odd_Squares(3, 4), 0)
        self.assertEqual(count_Odd_Squares(4, 4), 1)
        self.assertEqual(count_Odd_Squares(5, 4), 0)
