import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(odd_Num_Sum(5), 20250000)

    def test_boundary_condition(self):
        self.assertEqual(odd_Num_Sum(1), 1)

    def test_edge_condition(self):
        self.assertEqual(odd_Num_Sum(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            odd_Num_Sum(-5)
