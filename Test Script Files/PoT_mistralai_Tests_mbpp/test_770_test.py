import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(3), 233)
        self.assertEqual(odd_Num_Sum(5), 3313)
        self.assertEqual(odd_Num_Sum(10), 197685)

    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 3)
        self.assertEqual(odd_Num_Sum(4), 288)

    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(2147483647), 120710474057273962335)
