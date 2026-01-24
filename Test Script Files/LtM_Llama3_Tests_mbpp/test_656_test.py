import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 3, 4], 3), 2)
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 4, 5], 3), 4)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 0), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 4), 0)
        self.assertEqual(find_Min_Sum([], [], 0), 0)
        self.assertEqual(find_Min_Sum([1, 2, 3], [], 3), float('inf'))
        self.assertEqual(find_Min_Sum([], [1, 2, 3], 3), float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Min_Sum('a', [1, 2, 3], 3)
        with self.assertRaises(TypeError):
            find_Min_Sum([1, 2, 3], 'a', 3)
        with self.assertRaises(TypeError):
            find_Min_Sum([1, 2, 3], [1, 2, 3], 'a')
