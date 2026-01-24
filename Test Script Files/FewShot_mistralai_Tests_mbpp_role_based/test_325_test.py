import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_Min_Squares(0), 0)

    def test_one(self):
        self.assertEqual(get_Min_Squares(1), 1)

    def test_two(self):
        self.assertEqual(get_Min_Squares(2), 2)

    def test_three(self):
        self.assertEqual(get_Min_Squares(3), 3)

    def test_four(self):
        self.assertEqual(get_Min_Squares(4), 2)

    def test_five(self):
        self.assertEqual(get_Min_Squares(5), 3)

    def test_negative_number(self):
        self.assertRaises(ValueError, get_Min_Squares, -1)

    def test_large_number(self):
        self.assertEqual(get_Min_Squares(100), 10)
