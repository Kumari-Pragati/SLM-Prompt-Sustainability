import unittest
from mbpp_770_code import odd_Num_Sum

class TestOdd_Num_Sum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(5), 36125)

    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(1), 0)
        self.assertEqual(odd_Num_Sum(2), 1)

    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(3), 225)
        self.assertEqual(odd_Num_Sum(4), 225)

    def test_tricky_case(self):
        self.assertEqual(odd_Num_Sum(10), 1234325)
