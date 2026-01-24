import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
        self.assertEqual(Check_Solution(-1, 1, 1), "No")
        self.assertEqual(Check_Solution(1, -1, 1), "No")
        self.assertEqual(Check_Solution(1, 1, -1), "No")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1e308, 1, 1), "No")
        self.assertEqual(Check_Solution(-1e308, 1, 1), "No")
        self.assertEqual(Check_Solution(1, 1e308, 1), "No")
        self.assertEqual(Check_Solution(1, 1, -1e308), "No")
