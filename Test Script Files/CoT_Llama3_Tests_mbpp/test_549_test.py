import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(5), 225)

    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 0)

    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(3), 225)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(-1)
