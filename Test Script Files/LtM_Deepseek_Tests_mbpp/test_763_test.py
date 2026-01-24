import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Min_Diff([1, 5, 3, 19, 18, 25], 6), 1)
        self.assertEqual(find_Min_Diff([4, 2, 1, 3], 4), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_Min_Diff([1], 1), 0)
        self.assertEqual(find_Min_Diff([], 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Diff([10**9, 10**9 + 1], 2), 1)
        self.assertEqual(find_Min_Diff([-10**9, -10**9 + 1], 2), 1)

    def test_complex_cases(self):
        self.assertEqual(find_Min_Diff([10, 20, 30, 40, 50], 5), 10)
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5, 6], 6), 1)
