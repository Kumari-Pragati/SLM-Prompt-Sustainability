import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(3), 331)
        self.assertEqual(odd_Num_Sum(5), 10889)

    def test_edge_and_boundary(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(100000), 1530157674807)
        self.assertEqual(odd_Num_Sum(17), 156635338377)

    def test_complex(self):
        self.assertEqual(odd_Num_Sum(21), 114065635338377)
        self.assertEqual(odd_Num_Sum(41), 114065635338377 * 2)
        self.assertEqual(odd_Num_Sum(61), 114065635338377 * 3)
