import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4], 4), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Min_Diff([10, 11, 12, 13], 4), 1)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Diff([1, 2], 2), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3], 1), 0)
        self.assertEqual(find_Min_Diff([1, 2, 3], 4), 10**20)
        self.assertEqual(find_Min_Diff([10**20, 10**20], 2), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Diff([], 1), 0)
        self.assertEqual(find_Min_Diff([10**20], 1), 0)
        self.assertEqual(find_Min_Diff([10**20, 10**20], 2), 0)

    def test_complex_cases(self):
        self.assertEqual(find_Min_Diff([1, 1, 2, 2, 3, 3], 6), 0)
        self.assertEqual(find_Min_Diff([1, 1, 1, 2, 2, 3], 6), 0)
        self.assertEqual(find_Min_Diff([10**20, 10**20 - 1, 10**20], 3), 1)
