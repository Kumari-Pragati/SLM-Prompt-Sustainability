import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 3), (1, 4, 7))
        self.assertEqual(find_closet([10, 11, 12], [13, 14, 15], [16, 17, 18], 3, 3, 3), (10, 13, 16))

    def test_edge_cases(self):
        self.assertEqual(find_closet([], [], [], 0, 0, 0), (sys.maxsize, sys.maxsize, sys.maxsize))
        self.assertEqual(find_closet([1], [], [], 1, 0, 0), (1, sys.maxsize, sys.maxsize))
        self.assertEqual(find_closet([], [1], [], 0, 1, 0), (sys.maxsize, 1, sys.maxsize))
        self.assertEqual(find_closet([1], [1], [], 1, 1, 0), (1, 1, sys.maxsize))
        self.assertEqual(find_closet([1], [], [1], 1, 0, 1), (1, sys.maxsize, 1))
        self.assertEqual(find_closet([], [1], [1], 0, 1, 1), (sys.maxsize, 1, 1))

    def test_boundary_cases(self):
        self.assertEqual(find_closet([sys.maxsize - 1], [sys.maxsize], [sys.maxsize], 1, 1, 1), (sys.maxsize - 1, sys.maxsize, sys.maxsize))
        self.assertEqual(find_closet([sys.maxsize], [sys.maxsize - 1], [sys.maxsize], 1, 1, 1), (sys.maxsize, sys.maxsize - 1, sys.maxsize))
        self.assertEqual(find_closet([sys.maxsize], [sys.maxsize], [sys.maxsize - 1], 1, 1, 1), (sys.maxsize, sys.maxsize, sys.maxsize - 1))
