import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_find_Diff(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Diff([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5), 0)
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 5], 5), 1)
        self.assertEqual(find_Diff([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5), 2)
        self.assertEqual(find_Diff([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], 5), 3)
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], 5), 4)
        self.assertEqual(find_Diff([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5], 5), 4)
