import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_Squares(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(3, 3), 36)
        self.assertEqual(count_Squares(4, 4), 100)
        self.assertEqual(count_Squares(5, 5), 225)
        self.assertEqual(count_Squares(6, 6), 441)
        self.assertEqual(count_Squares(7, 7), 784)
        self.assertEqual(count_Squares(8, 8), 1296)
        self.assertEqual(count_Squares(9, 9), 2025)
        self.assertEqual(count_Squares(10, 10), 3025)

    def test_count_Squares_m_greater_than_n(self):
        self.assertEqual(count_Squares(5, 3), 36)
        self.assertEqual(count_Squares(4, 2), 6)
        self.assertEqual(count_Squares(3, 1), 1)

    def test_count_Squares_m_equal_to_n(self):
        self.assertEqual(count_Squares(5, 5), 225)
        self.assertEqual(count_Squares(4, 4), 100)
        self.assertEqual(count_Squares(3, 3), 36)
