import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(Check_Solution(1, 3, 2), "Yes")

    def test_edge_case_a(self):
        self.assertEqual(Check_Solution(0, 3, 2), "No")

    def test_edge_case_b(self):
        self.assertEqual(Check_Solution(1, 0, 2), "No")

    def test_edge_case_c(self):
        self.assertEqual(Check_Solution(1, 3, 0), "No")

    def test_edge_case_d(self):
        self.assertEqual(Check_Solution(1, 3, 1), "No")

    def test_complex_case(self):
        self.assertEqual(Check_Solution(2, 4, 1.5), "Yes")
