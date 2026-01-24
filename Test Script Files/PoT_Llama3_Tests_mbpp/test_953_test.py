import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(subset([1, 2, 2, 3, 4, 4, 5, 6, 6], 6), 4)

    def test_edge_case(self):
        self.assertEqual(subset([1, 1, 1, 1, 1], 5), 5)

    def test_edge_case2(self):
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case3(self):
        self.assertEqual(subset([], 0), 0)

    def test_edge_case4(self):
        self.assertEqual(subset([1], 1), 1)

    def test_edge_case5(self):
        self.assertEqual(subset([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 1)
