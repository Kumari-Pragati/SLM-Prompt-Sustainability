import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_pair_OR_Sum(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6], 6), 6)
        self.assertEqual(pair_OR_Sum([1, 1, 1, 1, 1], 5, ), 0)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7], 7), 7)
        self.assertEqual(pair_OR_Sum([1, 2, 3, 4, 5, 6, 7, 8], 8, ), 8)
