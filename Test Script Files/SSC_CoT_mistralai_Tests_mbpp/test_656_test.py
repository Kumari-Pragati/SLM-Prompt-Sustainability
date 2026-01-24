import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 2)
        self.assertEqual(find_Min_Sum([-1, 0, 1], [-2, -1, 0], 3), 1)
        self.assertEqual(find_Min_Sum([5, 3, 2], [6, 4, 1], 3), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([1], [], 0), 1)
        self.assertEqual(find_Min_Sum([1], [1], 0), 0)
        self.assertEqual(find_Min_Sum([1], [2], 1), 1)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2], 2), 0)
        self.assertEqual(find_Min_Sum([1, 2], [1, 3], 2), 1)
        self.assertEqual(find_Min_Sum([1, 2], [1, 2, 3], 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Sum([-1, -2, -3], [-4, -5, -6], 3), 15)
        self.assertEqual(find_Min_Sum([-1, 0, 1], [-2, -1, 0], 3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Min_Sum('a', 'b', 1)
        with self.assertRaises(TypeError):
            find_Min_Sum([1], 2, 1)
        with self.assertRaises(IndexError):
            find_Min_Sum([1], [0], 1)
