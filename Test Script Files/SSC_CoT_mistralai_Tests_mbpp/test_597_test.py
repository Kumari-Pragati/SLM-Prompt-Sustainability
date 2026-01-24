import unittest
from mbpp_597_code import find_kth

class TestFindKth(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_kth([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5, 5, 5), 5)
        self.assertEqual(find_kth([1, 2, 3], [4, 5, 6], 3, 3, 2), 3)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(find_kth([], [], 0, 0, 1), None)
        self.assertEqual(find_kth([1], [], 1, 0, 1), 1)
        self.assertEqual(find_kth([], [1], 0, 1, 1), 1)
        self.assertEqual(find_kth([1], [1], 1, 1, 1), 1)
        self.assertEqual(find_kth([1], [1], 1, 1, 2), None)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_kth, 'a', 'b', 1, 2, 3)
        self.assertRaises(TypeError, find_kth, [1, 2], 'b', 1, 2, 3)
        self.assertRaises(TypeError, find_kth, [1, 2], [3, 4], 'k', 1, 2)
        self.assertRaises(ValueError, find_kth, [1, 2], [3, 4], 1, -1, 2)
        self.assertRaises(ValueError, find_kth, [1, 2], [3, 4], 1, 1, -1)
        self.assertRaises(ValueError, find_kth, [1, 2], [3, 4], 0, 1, 0)
        self.assertRaises(ValueError, find_kth, [1, 2], [3, 4], 0, 1, len([1, 2]) + len([3, 4]) + 1)
