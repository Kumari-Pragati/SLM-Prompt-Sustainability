import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)

    def test_edge(self):
        self.assertEqual(min_Num([], 0), 2)
        self.assertEqual(min_Num([1], 1), 2)
        self.assertEqual(min_Num([2], 1), 2)

    def test_odd(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 2)
        self.assertEqual(min_Num([1, 3, 5, 7, 11], 5), 1)
        self.assertEqual(min_Num([1, 3, 5, 7, 9, 11], 6), 1)

    def test_even(self):
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)
        self.assertEqual(min_Num([2, 4, 6, 8, 12], 5), 2)
        self.assertEqual(min_Num([2, 4, 6, 8, 10, 12], 6), 2)
