import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_Min_Squares(0), 0)

    def test_single_element(self):
        self.assertEqual(get_Min_Squares(1), 1)

    def test_small_numbers(self):
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)

    def test_large_numbers(self):
        self.assertEqual(get_Min_Squares(10), 4)
        self.assertEqual(get_Min_Squares(20), 9)
        self.assertEqual(get_Min_Squares(30), 16)

    def test_large_and_small_combinations(self):
        self.assertEqual(get_Min_Squares(15), 4)
        self.assertEqual(get_Min_Squares(28), 9)
        self.assertEqual(get_Min_Squares(49), 16)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, get_Min_Squares, -1)
