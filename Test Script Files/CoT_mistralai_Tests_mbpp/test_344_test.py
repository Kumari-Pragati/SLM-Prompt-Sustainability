import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_Odd_Squares(1, 25), 3)
        self.assertEqual(count_Odd_Squares(26, 36), 1)
        self.assertEqual(count_Odd_Squares(49, 64), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(0, 4), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(16, 25), 3)
        self.assertEqual(count_Odd_Squares(26, 25), 0)
        self.assertEqual(count_Odd_Squares(625, 626), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 4), 0)
        self.assertEqual(count_Odd_Squares(4, 1), 0)
        self.assertEqual(count_Odd_Squares(9, 16), 0)
        self.assertEqual(count_Odd_Squares(16, 9), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, count_Odd_Squares, -1, 4)
        self.assertRaises(ValueError, count_Odd_Squares, 1, -1)
        self.assertRaises(ValueError, count_Odd_Squares, 0, 0)
