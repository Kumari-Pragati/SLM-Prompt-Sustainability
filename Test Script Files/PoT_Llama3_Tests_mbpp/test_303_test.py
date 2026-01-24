import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_edge_case2(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 1))

    def test_edge_case3(self):
        self.assertFalse(solve([5, 5, 5, 5, 5], 5))

    def test_edge_case4(self):
        self.assertFalse(solve([1, 2, 3, 4, 5], 0))

    def test_edge_case5(self):
        self.assertFalse(solve([1, 2, 3, 4, 5], 6))

    def test_edge_case6(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6], 6))

    def test_edge_case7(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7], 7))

    def test_edge_case8(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8], 8))

    def test_edge_case9(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_edge_case10(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
