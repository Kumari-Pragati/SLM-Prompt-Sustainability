import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(2, 1, 2), "Yes")
        self.assertEqual(Check_Solution(-1, -2, -1), "Yes")

    def test_edge_case(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")
        self.assertEqual(Check_Solution(1, 1, 0), "No")

    def test_boundary_case(self):
        self.assertEqual(Check_Solution(-1, 0, -1), "Yes")
        self.assertEqual(Check_Solution(1, 0, -1), "No")
        self.assertEqual(Check_Solution(-1, -1, 0), "No")
