import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 4)
        self.assertEqual(pair_OR_Sum([4, 5, 6], 3), 15)
        self.assertEqual(pair_OR_Sum([7, 8, 9], 3), 21)

    def test_edge_and_boundary(self):
        self.assertEqual(pair_OR_Sum([0, 0, 0], 3), 0)
        self.assertEqual(pair_OR_Sum([2147483647, 2147483647], 1), 2147483646)
        self.assertEqual(pair_OR_Sum([], 0), 0)
        self.assertEqual(pair_OR_Sum([1], 1), 0)
        self.assertEqual(pair_OR_Sum([1, 1], 2), 0)

    def test_complex(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(pair_OR_Sum([5, 4, 3, 2, 1], 5), 15)
        self.assertEqual(pair_OR_Sum([2147483647, 2147483646, 2147483645], 3), 2147483644)
