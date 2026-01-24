import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_Squares(self):
        self.assertEqual(count_Squares(2, 3), 6)
        self.assertEqual(count_Squares(3, 2), 6)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(5, 5), 30)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(-1, 1), 1)
        self.assertEqual(count_Squares(1, -1), 1)
        self.assertEqual(count_Squares(-1, -1), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 1), 0)
        self.assertEqual(count_Squares(-1, 0), 0)
        self.assertEqual(count_Squares(0, -1), 0)
