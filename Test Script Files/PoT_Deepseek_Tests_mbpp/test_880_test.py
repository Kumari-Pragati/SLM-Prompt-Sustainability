import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Check_Solution(1, -3, 2), "2 solutions")
        self.assertEqual(Check_Solution(1, 0, 1), "1 solution")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(1, 0, 0), "1 solution")
        self.assertEqual(Check_Solution(0, 0, 0), "1 solution")

    def test_boundary_cases(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No solutions")
        self.assertEqual(Check_Solution(1, -1, 1), "No solutions")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)
        with self.assertRaises(TypeError):
            Check_Solution(1, 2)
