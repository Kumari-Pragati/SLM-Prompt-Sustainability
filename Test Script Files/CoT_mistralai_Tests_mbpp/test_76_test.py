import unittest
from76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 5), 9)
        self.assertEqual(count_Squares(5, 3), 9)

    def test_edge_case_equal_sides(self):
        self.assertEqual(count_Squares(4, 4), 10)

    def test_edge_case_one_side(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(1, 5), 6)
        self.assertEqual(count_Squares(5, 1), 1)

    def test_invalid_input_non_positive(self):
        self.assertRaises(ValueError, count_Squares, -1, 2)
        self.assertRaises(ValueError, count_Squares, 2, -1)

    def test_invalid_input_zero(self):
        self.assertRaises(ValueError, count_Squares, 0, 2)
        self.assertRaises(ValueError, count_Squares, 2, 0)
