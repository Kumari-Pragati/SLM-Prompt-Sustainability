import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_typical_case_2(self):
        self.assertEqual(Check_Solution(2, 4, 8), "Yes")

    def test_edge_case_zero_a(self):
        self.assertEqual(Check_Solution(0, 2, 3), "No")

    def test_edge_case_zero_b(self):
        self.assertEqual(Check_Solution(1, 0, 3), "No")

    def test_edge_case_zero_c(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No")

    def test_edge_case_negative_a(self):
        self.assertEqual(Check_Solution(-1, 2, 3), "No")

    def test_edge_case_negative_b(self):
        self.assertEqual(Check_Solution(1, -2, 3), "No")

    def test_edge_case_negative_c(self):
        self.assertEqual(Check_Solution(1, 2, -3), "No")

    def test_edge_case_negative_values(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "No")

    def test_error_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 2, 3)
