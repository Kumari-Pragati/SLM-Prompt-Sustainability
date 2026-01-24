import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4], 5), 0)
        self.assertEqual(find_Diff([1, 1, 2, 2, 3], 5), 1)
        self.assertEqual(find_Diff([1, 1, 1, 2, 2], 5), 2)

    def test_edge_cases(self):
        self.assertEqual(find_Diff([1, 1, 1], 3), 0)
        self.assertEqual(find_Diff([1, 1, 1, 1], 4), 0)
        self.assertEqual(find_Diff([], 0), 0)
        self.assertEqual(find_Diff([1], 1), 0)
        self.assertEqual(find_Diff([1, 1], 2), 0)

    def test_boundary_cases(self):
        self.assertEqual(find_Diff([2**31 - 1, 2**31 - 1], 2), 0)
        self.assertEqual(find_Diff([2**31 - 1, 2**31], 2), 1)
        self.assertEqual(find_Diff([2**31], 1), 0)
