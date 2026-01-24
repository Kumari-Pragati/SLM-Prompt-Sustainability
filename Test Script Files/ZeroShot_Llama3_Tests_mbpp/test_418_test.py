import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(Find_Max([10, 20, 30, 40, 50]), 50)
        self.assertEqual(Find_Max([-10, -20, -30, -40, -50]), -50)
        self.assertEqual(Find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(Find_Max([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), -1)
        self.assertEqual(Find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 15)
        self.assertEqual(Find_Max([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), -1)
        self.assertEqual(Find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 20)
        self.assertEqual(Find_Max([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]), -1)
