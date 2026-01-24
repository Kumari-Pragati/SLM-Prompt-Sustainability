import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 3, 2), "Yes")
        self.assertEqual(Check_Solution(2, 4, 1), "Yes")
        self.assertEqual(Check_Solution(3, 9, 1), "Yes")

    def test_edge_case_a(self):
        self.assertEqual(Check_Solution(0, 3, 2), "No")
        self.assertEqual(Check_Solution(1, 0, 2), "No")
        self.assertEqual(Check_Solution(1, 3, 0), "No")

    def test_edge_case_b(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")
        self.assertEqual(Check_Solution(1, 2, 2), "No")
        self.assertEqual(Check_Solution(2, 1, 1), "No")

    def test_corner_case(self):
        self.assertEqual(Check_Solution(1, 9, 9), "Yes")
        self.assertEqual(Check_Solution(9, 1, 9), "Yes")
        self.assertEqual(Check_Solution(9, 9, 1), "Yes")
