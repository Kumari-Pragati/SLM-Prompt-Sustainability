import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(count_Squares(3, 5), 9)
        self.assertEqual(count_Squares(5, 5), 6)
        self.assertEqual(count_Squares(10, 10), 28)

    def test_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(0, 5), 0)
        self.assertEqual(count_Squares(5, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Squares(-3, 5), 9)
        self.assertEqual(count_Squares(5, -3), 9)
        self.assertEqual(count_Squares(-3, -5), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 1), 0)
