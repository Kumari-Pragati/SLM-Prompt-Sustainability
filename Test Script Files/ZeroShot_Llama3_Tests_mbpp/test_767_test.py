import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_get_Pairs_Count(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 7), 2)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 9), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 10), 0)
        self.assertEqual(get_Pairs_Count([1, 1, 1, 1, 1], 5, 2), 4)
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([1, 2], 2, 3), 1)
