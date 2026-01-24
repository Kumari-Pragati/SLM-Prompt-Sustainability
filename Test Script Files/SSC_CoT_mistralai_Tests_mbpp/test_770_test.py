import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(odd_Num_Sum(3), 3375)
        self.assertEqual(odd_Num_Sum(5), 33749)
        self.assertEqual(odd_Num_Sum(10), 1357675)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 3)
        self.assertEqual(odd_Num_Sum(4), 3375)
        self.assertEqual(odd_Num_Sum(100), 26744479401)
        self.assertEqual(odd_Num_Sum(1000), 2088606451835225)

    def test_invalid_input(self):
        self.assertRaises(TypeError, odd_Num_Sum, "not_a_number")
        self.assertRaises(TypeError, odd_Num_Sum, -1)
        self.assertRaises(TypeError, odd_Num_Sum, 0)
