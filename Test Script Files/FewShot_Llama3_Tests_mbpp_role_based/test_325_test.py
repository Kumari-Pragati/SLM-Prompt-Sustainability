import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(3), 3)

    def test_medium_numbers(self):
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(5), 1)
        self.assertEqual(get_Min_Squares(6), 3)

    def test_large_numbers(self):
        self.assertEqual(get_Min_Squares(10), 3)
        self.assertEqual(get_Min_Squares(12), 3)
        self.assertEqual(get_Min_Squares(15), 4)

    def test_edge_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(3), 3)
