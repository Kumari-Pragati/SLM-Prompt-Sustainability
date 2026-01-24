import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(3), 153)
        self.assertEqual(odd_Num_Sum(5), 3375)
        self.assertEqual(odd_Num_Sum(10), 262143)

    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 3)

    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(2147483647), 1316434415968265401)
