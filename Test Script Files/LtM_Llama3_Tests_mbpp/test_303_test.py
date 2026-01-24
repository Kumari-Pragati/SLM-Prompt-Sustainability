import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_empty(self):
        self.assertFalse(solve([], 1))

    def test_edge_single(self):
        self.assertTrue(solve([1], 1))

    def test_edge_max(self):
        self.assertTrue(solve([sys.maxsize - 1, sys.maxsize - 1, sys.maxsize - 1], 3))

    def test_edge_min(self):
        self.assertTrue(solve([-sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1], 3))

    def test_edge_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1], 3))

    def test_edge_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, sys.maxsize - 1], 4))

    def test_edge_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1], 4))

    def test_edge_max_min_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1], 5))

    def test_edge_max_min_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1], 5))

    def test_edge_max_min_max_min_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, sys.maxsize - 1], 6))

    def test_edge_max_min_max_min_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1], 6))

    def test_edge_max_min_max_min_max_min_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1], 7))

    def test_edge_max_min_max_min_max_min_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1], 7))

    def test_edge_max_min_max_min_max_min_max_min_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1], 8))

    def test_edge_max_min_max_min_max_min_max_min_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1], 8))

    def test_edge_max_min_max_min_max_min_max_min_max_min_max_min_max(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1], 9))

    def test_edge_max_min_max_min_max_min_max_min_max_min_max_min_max_min(self):
        self.assertTrue(solve([sys.maxsize - 1, -sys.maxsize - 1, sys.maxsize - 1, -sys.maxsize - 1, sys.max