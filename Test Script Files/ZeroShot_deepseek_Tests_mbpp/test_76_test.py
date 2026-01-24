import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_squares(self):
        self.assertEqual(count_Squares(2, 3), 14)
        self.assertEqual(count_Squares(5, 5), 45)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(10, 2), 65)
