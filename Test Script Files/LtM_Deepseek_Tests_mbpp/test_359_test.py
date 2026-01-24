import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(Check_Solution(1, 2, 4), "Yes")

    def test_edge_case_zero_a(self):
        self.assertEqual(Check_Solution(0, 2, 4), "No")

    def test_boundary_case_negative_a(self):
        self.assertEqual(Check_Solution(-1, 2, 4), "No")

    def test_edge_case_zero_b(self):
        self.assertEqual(Check_Solution(1, 0, 4), "No")

    def test_boundary_case_negative_b(self):
        self.assertEqual(Check_Solution(1, -2, 4), "No")

    def test_edge_case_zero_c(self):
        self.assertEqual(Check_Solution(1, 2, 0), "Yes")

    def test_boundary_case_negative_c(self):
        self.assertEqual(Check_Solution(1, 2, -4), "No")

    def test_complex_case(self):
        self.assertEqual(Check_Solution(2, 4, 16), "Yes")
