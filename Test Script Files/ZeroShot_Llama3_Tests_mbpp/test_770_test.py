import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_odd_Num_Sum(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 0)
        self.assertEqual(odd_Num_Sum(3), 14)
        self.assertEqual(odd_Num_Sum(4), 0)
        self.assertEqual(odd_Num_Sum(5), 35)
        self.assertEqual(odd_Num_Sum(6), 0)
        self.assertEqual(odd_Num_Sum(7), 70)
        self.assertEqual(odd_Num_Sum(8), 0)
        self.assertEqual(odd_Num_Sum(9), 126)
        self.assertEqual(odd_Num_Sum(10), 0)

    def test_edge_cases(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(-1), 0)
