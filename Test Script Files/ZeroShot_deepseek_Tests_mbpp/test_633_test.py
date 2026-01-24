import unittest
from mbpp_633_code import pair_OR_Sum

class TestPairORSum(unittest.TestCase):

    def test_pair_OR_Sum(self):
        self.assertEqual(pair_OR_Sum([1, 2, 3], 3), 6)
        self.assertEqual(pair_OR_Sum([4, 5, 6], 3), 4)
        self.assertEqual(pair_OR_Sum([7, 8, 9], 3), 0)
        self.assertEqual(pair_OR_Sum([10, 11, 12], 3), 12)
        self.assertEqual(pair_OR_Sum([13, 14, 15], 3), 8)
