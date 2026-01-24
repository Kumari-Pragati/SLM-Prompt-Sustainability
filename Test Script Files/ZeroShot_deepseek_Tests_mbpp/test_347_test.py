import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_Squares(self):
        self.assertEqual(count_Squares(2, 3), 6)
        self.assertEqual(count_Squares(5, 7), 245)
        self.assertEqual(count_Squares(10, 1), 55)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 4)
        self.assertEqual(count_Squares(3, 2), 6)
        self.assertEqual(count_Squares(4, 5), 35)
        self.assertEqual(count_Squares(6, 7), 105)
