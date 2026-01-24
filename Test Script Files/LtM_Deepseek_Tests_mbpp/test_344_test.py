import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(1, 9), 2)

    def test_edge_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 2), 0)
        self.assertEqual(count_Odd_Squares(1, 3), 1)
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(1, 5), 1)
        self.assertEqual(count_Odd_Squares(1, 6), 1)
        self.assertEqual(count_Odd_Squares(1, 7), 1)
        self.assertEqual(count_Odd_Squares(1, 8), 1)
        self.assertEqual(count_Odd_Squares(1, 9), 2)

    def test_complex_cases(self):
        self.assertEqual(count_Odd_Squares(1, 100), 7)
        self.assertEqual(count_Odd_Squares(1, 1000), 31)
