import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(get_Min_Squares(0), 0)

    def test_one(self):
        self.assertEqual(get_Min_Squares(1), 1)

    def test_two(self):
        self.assertEqual(get_Min_Squares(2), 1)

    def test_three(self):
        self.assertEqual(get_Min_Squares(3), 1)

    def test_four(self):
        self.assertEqual(get_Min_Squares(4), 2)

    def test_five(self):
        self.assertEqual(get_Min_Squares(5), 2)

    def test_six(self):
        self.assertEqual(get_Min_Squares(6), 3)

    def test_seven(self):
        self.assertEqual(get_Min_Squares(7), 3)

    def test_eight(self):
        self.assertEqual(get_Min_Squares(8), 4)

    def test_nine(self):
        self.assertEqual(get_Min_Squares(9), 4)

    def test_ten(self):
        self.assertEqual(get_Min_Squares(10), 5)

    def test_twenty(self):
        self.assertEqual(get_Min_Squares(20), 9)

    def test_hundred(self):
        self.assertEqual(get_Min_Squares(100), 16)
