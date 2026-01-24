import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")

    def test_edge_case_a_eq_c(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_case_b_eq_c(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_case_a_eq_b(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_case_a_neq_b_neq_c(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_edge_case_a_eq_b_neq_c(self):
        self.assertEqual(Check_Solution(1, 1, 2), "No")

    def test_edge_case_a_neq_b_eq_c(self):
        self.assertEqual(Check_Solution(1, 2, 1), "No")

    def test_edge_case_a_eq_b_eq_c(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")
