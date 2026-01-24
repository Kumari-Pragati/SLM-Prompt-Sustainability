import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case1(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6], 6))

    def test_edge_case2(self):
        self.assertTrue(solve([5, 4, 3, 2, 1], 5))

    def test_edge_case3(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7], 7))

    def test_edge_case4(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8], 8))

    def test_edge_case5(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_edge_case6(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

    def test_edge_case7(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11))

    def test_edge_case8(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12))

    def test_edge_case9(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13))

    def test_edge_case10(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14))

    def test_edge_case11(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15))

    def test_edge_case12(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16))

    def test_edge_case13(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17))

    def test_edge_case14(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18))

    def test_edge_case15(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19))

    def test_edge_case16(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20))

    def test_edge_case17(self):
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21))

    def test_edge_case18(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7, 8, 9