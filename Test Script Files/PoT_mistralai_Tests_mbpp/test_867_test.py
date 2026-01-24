import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_Num([1, 3, 2, 4, 5], 5), 1)
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(min_Num([-1, -3, -2, -4, -5], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(min_Num([1], 1), 1)
        self.assertEqual(min_Num([2], 1), 2)
        self.assertEqual(min_Num([], 0), None)
        self.assertEqual(min_Num([1, 2, 3], 1), 1)
        self.assertEqual(min_Num([1, 2, 3], 3), 1)
        self.assertEqual(min_Num([1, 2, 3], 4), 2)
