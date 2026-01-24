import unittest
from mbpp_31_code import defaultdict
from heapq import heappush, heappop

from thirty_one_code import func

class TestFunc(unittest.TestCase):

    def test_normal_case(self):
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [1, 2, 3])
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [1, 2])
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [1])

    def test_edge_cases(self):
        self.assertListEqual(func([[1], [2], [3]], 2), [1, 2])
        self.assertListEqual(func([[1], [2], [3]], 1), [1])
        self.assertListEqual(func([[], [2], [3]], 1), [2])
        self.assertListEqual(func([[1], [], [3]], 1), [1])
        self.assertListEqual(func([[1], [2], []], 1), [2])

    def test_boundary_cases(self):
        self.assertListEqual(func([[1]], 1), [1])
        self.assertListEqual(func([[1, 2]], 1), [2])
        self.assertListEqual(func([[1, 2], [1, 2]], 1), [1])
        self.assertListEqual(func([[1, 2], [1, 2]], 2), [1, 2])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, func, [1, 2, 3], 'k')
        self.assertRaises(TypeError, func, ['a', 'b', 'c'], 3)
        self.assertRaises(TypeError, func, [[1, 2], [3, 4]], 0)
        self.assertRaises(TypeError, func, [[1, 2], [3, 4]], -1)
