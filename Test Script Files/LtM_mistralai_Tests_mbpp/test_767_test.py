import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(get_Pairs_Count([10, 15, 3, 7], 4, 17), 1)

    def test_edge_cases(self):
        self.assertEqual(get_Pairs_Count([], 0, 1), 0)
        self.assertEqual(get_Pairs_Count([1], 1, 1), 0)
        self.assertEqual(get_Pairs_Count([1, 2], 2, 3), 0)
        self.assertEqual(get_Pairs_Count([1, 2], 2, 4), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 2], 3, 4), 2)

    def test_boundary_conditions(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 0), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 4, 7), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 1, 5), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4], 5, 5), 4)
