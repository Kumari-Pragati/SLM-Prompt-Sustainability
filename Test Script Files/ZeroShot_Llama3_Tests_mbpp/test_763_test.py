import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_find_min_diff(self):
        self.assertEqual(find_Min_Diff([1, 3, 5, 2, 4], 5), 1)
        self.assertEqual(find_Min_Diff([10, 20, 30, 40, 50], 5), 10)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_Min_Diff([5, 5, 5, 5, 5], 5), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 6), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7], 7), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8], 8), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 1)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)

    def test_find_min_diff_edge_cases(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)
        self.assertEqual(find_Min_Diff([1, 1], 2), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1], 3), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1, 1], 4), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1, 1, 1], 5), 0)
