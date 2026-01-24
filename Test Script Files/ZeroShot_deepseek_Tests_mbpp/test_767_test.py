import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_get_Pairs_Count(self):
        self.assertEqual(get_Pairs_Count([1, 1, 1, 1], 4, 2), 6)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 2)
        self.assertEqual(get_Pairs_Count([1, 5, 7, 1], 4, 6), 1)
        self.assertEqual(get_Pairs_Count([0, 0, 0, 0], 4, 0), 6)
        self.assertEqual(get_Pairs_Count([10, 12, 10, 15, 26, 14, 25, 26], 8, 31), 3)
