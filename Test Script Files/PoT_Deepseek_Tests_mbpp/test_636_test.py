import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(10, 10, 10), "Yes")
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Check_Solution(-1, -1, -1), "Yes")
        self.assertEqual(Check_Solution(float('inf'), float('inf'), float('inf')), "Yes")
        self.assertEqual(Check_Solution(float('-inf'), float('-inf'), float('-inf')), "Yes")

    def test_corner_cases(self):
        self.assertEqual(Check_Solution(float('nan'), float('nan'), float('nan')), "No")
        self.assertEqual(Check_Solution(None, None, None), "No")
        self.assertEqual(Check_Solution(True, True, True), "Yes")
        self.assertEqual(Check_Solution(False, False, False), "Yes")
