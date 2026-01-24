import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(find_Sum([-1, 0, 1, 2, 3], 5), 6)

    def test_edge_cases(self):
        self.assertEqual(find_Sum([1], 1), 1)
        self.assertEqual(find_Sum([1, 1], 2), 1)
        self.assertEqual(find_Sum([1, 2, 1], 3), 3)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5, 6], 6), 15)

    def test_boundary_cases(self):
        self.assertEqual(find_Sum([-10, -9, -8, -7, -6], 5), -28)
        self.assertEqual(find_Sum([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(find_Sum([10, 20, 30, 40, 50], 5), 140)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Sum, [1, 2, 3], 'n')
        self.assertRaises(TypeError, find_Sum, ['1', '2', '3'], 3)
        self.assertRaises(ValueError, find_Sum, [], 0)
        self.assertRaises(ValueError, find_Sum, [1], 0)
