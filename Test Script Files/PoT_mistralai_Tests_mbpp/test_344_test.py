import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 3)
        self.assertEqual(count_Odd_Squares(10, 121), 15)
        self.assertEqual(count_Odd_Squares(20, 225), 25)

    def test_edge_case(self):
        self.assertEqual(count_Odd_Squares(0, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 1), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(4, 9), 1)
        self.assertEqual(count_Odd_Squares(9, 16), 1)

    def test_negative_case(self):
        self.assertRaises(ValueError, count_Odd_Squares, -1, 4)
        self.assertRaises(ValueError, count_Odd_Squares, 1, -1)
