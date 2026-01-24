import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_find_Diff(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3], 6), 2)
        self.assertEqual(find_Diff([1, 2, 2, 3, 3, 4, 4, 5, 5], 9), 2)
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), 0)
        self.assertEqual(find_Diff([10, 20, 30, 40, 50], 5), 0)
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 1)
