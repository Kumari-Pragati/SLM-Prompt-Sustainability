import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, 9))
        self.assertEqual(find_minimum_range([[10, 11, 12], [13, 14, 15], [16, 17, 18]])), (10, 18))

    def test_edge_cases(self):
        self.assertEqual(find_minimum_range([[1], [2], [3]]), (1, 3))
        self.assertEqual(find_minimum_range([[10], [20], [30]]), (10, 30))
        self.assertEqual(find_minimum_range([[1, 2, 3], [4], [5, 6]]), (1, 6))
        self.assertEqual(find_minimum_range([[1, 2, 3], [], [5, 6]]), (1, 6))

    def test_boundary_conditions(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5], [6]]), (1, 6))
        self.assertEqual(find_minimum_range([[1, 2, 3], [], [6]]), (1, 6))
        self.assertEqual(find_minimum_range([[], [4, 5], [6]]), (None, None))
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5], []]), (1, 5))

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_minimum_range, [1, 2, 3])
        self.assertRaises(TypeError, find_minimum_range, [[1, 2], 3])
        self.assertRaises(TypeError, find_minimum_range, [1, [2, 3]])
