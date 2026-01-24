import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 3)
        self.assertEqual(find_Min_Sum([10, 20, 30], [40, 50, 60], 3), 90)

    def test_edge_conditions(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([1], [1], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)
        self.assertEqual(find_Min_Sum([100], [200], 1), 100)
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5), 14)

    def test_complex_cases(self):
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5), 14)
        self.assertEqual(find_Min_Sum([10, 20, 30, 40, 50], [60, 70, 80, 90, 100], 5), 150)
