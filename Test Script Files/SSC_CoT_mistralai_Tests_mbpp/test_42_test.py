import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4], 6), 4)
        self.assertEqual(find_Sum([1, 1, 1, 2, 3, 4], 6), 1)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5, 5], 6), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Sum([], 0), 0)
        self.assertEqual(find_Sum([1], 1), 1)
        self.assertEqual(find_Sum([1, 1], 2), 1)
        self.assertEqual(find_Sum([1, 2, 2, 2], 4), 2)
        self.assertEqual(find_Sum([1, 2, 2, 2, 2], 5), 2)

    def test_special_cases(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 2], 5), 1)
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(find_Sum([1, 1, 2, 2, 3], 5), 0)
