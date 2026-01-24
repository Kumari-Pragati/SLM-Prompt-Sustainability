import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 6)
        self.assertEqual(find_Min_Sum([-1, 0, 1], [-2, -1, 0], 3), 2)
        self.assertEqual(find_Min_Sum([0, 0, 0], [1, 1, 1], 3), 3)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([1], [], 1), 1)
        self.assertEqual(find_Min_Sum([1, 2], [], 2), 2)
        self.assertEqual(find_Min_Sum([1, 2], [3], 2), 2)
        self.assertEqual(find_Min_Sum([1, 2], [1, 3], 2), 2)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2, 3], 3), 0)

    def test_complex(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 1, 0], 3), 4)
        self.assertEqual(find_Min_Sum([10, 20, 30], [15, 5, 5], 3), 40)
        self.assertEqual(find_Min_Sum([100, 200, 300], [150, 50, 5], 3), 200)
