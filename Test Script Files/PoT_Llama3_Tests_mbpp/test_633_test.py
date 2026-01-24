import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 0)

    def test_edge(self):
        self.assertEqual(pair_OR_Sum([1, 1, 2, 2], 4), 0)

    def test_edge2(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 3), 0)

    def test_edge3(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 0)

    def test_edge4(self):
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1], 4), 0)

    def test_edge5(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_edge6(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6], 6), 0)

    def test_edge7(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7], 7), 0)

    def test_edge8(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)

    def test_edge9(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 0)

    def test_edge10(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
