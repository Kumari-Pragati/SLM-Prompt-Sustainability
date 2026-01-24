import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(odd_Num_Sum(1), 5)

    def test_boundary_conditions(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(2), 1365)

    def test_edge_cases(self):
        self.assertEqual(odd_Num_Sum(-1), 0)
        self.assertEqual(odd_Num_Sum(3), 1365)

    def test_complex_cases(self):
        self.assertEqual(odd_Num_Sum(10), 136500)
