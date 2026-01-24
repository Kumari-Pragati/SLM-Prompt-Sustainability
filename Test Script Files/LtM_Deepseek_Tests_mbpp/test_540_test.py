import unittest
from mbpp_540_code import find_Diff

class TestFindDiff(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6], 9), 2)
        self.assertEqual(find_Diff([10, 20, 30, 40, 50], 5), 0)

    def test_edge_conditions(self):
        self.assertEqual(find_Diff([], 0), 0)
        self.assertEqual(find_Diff([1], 1), 0)
        self.assertEqual(find_Diff([1, 1, 1, 1], 4), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Diff([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(find_Diff([5, 4, 3, 2, 1], 5), 0)

    def test_complex_cases(self):
        self.assertEqual(find_Diff([1, 2, 2, 3, 4, 4, 4, 5, 6, 6], 10), 1)
        self.assertEqual(find_Diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
