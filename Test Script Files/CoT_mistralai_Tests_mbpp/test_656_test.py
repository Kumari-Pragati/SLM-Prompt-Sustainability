import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 3)
        self.assertEqual(find_Min_Sum([0, 0, 0], [1, 1, 1], 3), 3)
        self.assertEqual(find_Min_Sum([-1, -2, -3], [1, 2, 3], 3), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([1], [], 1), 1)
        self.assertEqual(find_Min_Sum([1, 2], [], 2), 2)
        self.assertEqual(find_Min_Sum([1, 2], [1], 2), 0)
        self.assertEqual(find_Min_Sum([1, 2], [1, 1], 1), 0)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2], 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Min_Sum, 'a', 'b', 3)
        self.assertRaises(TypeError, find_Min_Sum, [1], 'b', 3)
        self.assertRaises(TypeError, find_Min_Sum, [1], [2], 'n')
        self.assertRaises(ValueError, find_Min_Sum, [1], [2], -1)
        self.assertRaises(ValueError, find_Min_Sum, [1], [2], len([1]) + len([2]) + 1)
