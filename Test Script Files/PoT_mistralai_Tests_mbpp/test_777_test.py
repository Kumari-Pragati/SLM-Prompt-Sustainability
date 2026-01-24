import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(find_Sum([0, 0, 1, 2, 3], 5), 6)
        self.assertEqual(find_Sum([-1, 0, 1, 2, 3], 5), 6)

    def test_edge_case(self):
        self.assertEqual(find_Sum([1], 1), 1)
        self.assertEqual(find_Sum([1, 1], 2), 1)
        self.assertEqual(find_Sum([1, 1, 1], 3), 1)
        self.assertEqual(find_Sum([], 0), 0)

    def test_boundary_case(self):
        self.assertEqual(find_Sum([-1000000, -999999, -999998, -999997, -999996], 5), -4999910)
        self.assertEqual(find_Sum([999996, 999997, 999998, 999999, 1000000], 5), 4999910)
