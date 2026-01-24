import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):

    def test_find_min_typical(self):
        self.assertEqual(find_Min([4, 6, 2, 8, 1, 3], 0, 5), 1)
        self.assertEqual(find_Min([-5, -3, -2, -1, 0], 0, 4), -5)
        self.assertEqual(find_Min([10, 12, 15, 19, 20], 0, 4), 10)

    def test_find_min_edge(self):
        self.assertEqual(find_Min([1], 0, 0), 1)
        self.assertEqual(find_Min([], 0, 0), None)
        self.assertEqual(find_Min([1, 2], 0, 1), 1)
        self.assertEqual(find_Min([1, 2], 1, 1), 1)

    def test_find_min_invalid(self):
        self.assertRaises(IndexError, lambda: find_Min([1, 2], -1, 0))
        self.assertRaises(IndexError, lambda: find_Min([1, 2], 2, 0))
