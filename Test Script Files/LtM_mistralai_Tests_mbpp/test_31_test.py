import unittest
from mbpp_31_code import defaultdict
from heapq import heappush, heappop

class TestFunc(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [1, 2, 3])
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [1, 2])
        self.assertListEqual(func([[6, 7, 8], [1, 2, 3], [4, 5, 9]], 2), [6, 7])

    def test_edge_cases(self):
        self.assertListEqual(func([], 3), [])
        self.assertListEqual(func([[1]], 1), [1])
        self.assertListEqual(func([[1, 1, 1], [2, 2, 2]], 2), [1, 2])
        self.assertListEqual(func([[1, 1, 1], [2, 2, 2]], 3), [1, 2, 1])

    def test_complex(self):
        self.assertListEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3), [1, 2, 3])
        self.assertListEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 2), [1, 2])
        self.assertListEqual(func([[1000000001, 1000000002, 1000000003], [1, 2, 3], [4, 5, 6]], 2), [1000000001, 1000000002])
