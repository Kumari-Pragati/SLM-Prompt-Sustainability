import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_boundary_case_zero_b(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_boundary_case_non_zero_b(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_edge_case_negative_values(self):
        self.assertEqual(Check_Solution(-1, 0, -1), "Yes")

    def test_edge_case_large_values(self):
        self.assertEqual(Check_Solution(1000000, 0, 1000000), "Yes")

    def test_edge_case_zero_a_and_b(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_case_zero_c(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
