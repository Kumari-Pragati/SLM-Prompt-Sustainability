import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(5), 22525)

    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(1), 0)
        self.assertEqual(odd_Num_Sum(2), 1)
        self.assertEqual(odd_Num_Sum(3), 225)

    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(4), 22525)
        self.assertEqual(odd_Num_Sum(5), 22525)
        self.assertEqual(odd_Num_Sum(6), 45050)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum("five")
