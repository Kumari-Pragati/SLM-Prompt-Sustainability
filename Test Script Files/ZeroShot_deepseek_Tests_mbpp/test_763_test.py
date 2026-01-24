import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_find_Min_Diff(self):
        self.assertEqual(find_Min_Diff([1, 5, 3, 19, 18, 25], 6), 1)
        self.assertEqual(find_Min_Diff([10, 100, 200], 3), 100)
        self.assertEqual(find_Min_Diff([5, 10, 15], 3), 5)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_Min_Diff([10, 20, 30, 40, 50], 5), 10)
