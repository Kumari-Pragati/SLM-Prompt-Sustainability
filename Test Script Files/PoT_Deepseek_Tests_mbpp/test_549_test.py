import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 17)
        self.assertEqual(odd_Num_Sum(3), 193)

    def test_edge_cases(self):
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(odd_Num_Sum(100), 100100100100100100100100)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')
        with self.assertRaises(TypeError):
            odd_Num_Sum(None)
        with self.assertRaises(TypeError):
            odd_Num_Sum([])
