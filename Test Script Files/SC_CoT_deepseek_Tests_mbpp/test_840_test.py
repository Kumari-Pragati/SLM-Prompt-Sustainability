import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_boundary_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_boundary_case_b_not_zero(self):
        self.assertEqual(Check_Solution(1, 1, 0), "No")

    def test_edge_case_negative_values(self):
        self.assertEqual(Check_Solution(-1, 0, -1), "Yes")

    def test_edge_case_zero_values(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 0)
