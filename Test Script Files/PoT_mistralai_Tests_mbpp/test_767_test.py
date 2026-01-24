import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 3), 2)
        self.assertEqual(get_Pairs_Count([10, 15, 3, 7], 4, 13), 1)
        self.assertEqual(get_Pairs_Count([-1, 0, 2, -2, 1], 5, 0), 2)

    def test_edge_case(self):
        self.assertEqual(get_Pairs_Count([], 0, 0), 0)
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([1, 1], 2, 2), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 6), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 0), 0)

    def test_corner_case(self):
        self.assertEqual(get_Pairs_Count([float('inf')], 1, float('inf')), 0)
        self.assertEqual(get_Pairs_Count([-float('inf')], 1, -float('inf')), 0)
