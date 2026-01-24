import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(Check_Solution(1, 3, 3), "Yes")
        self.assertEqual(Check_Solution(4, 2, 1), "Yes")
        self.assertEqual(Check_Solution(9, 1, 1), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(0, 3, 3), "No")
        self.assertEqual(Check_Solution(1, 0, 3), "No")
        self.assertEqual(Check_Solution(1, 3, 0), "No")
        self.assertEqual(Check_Solution(-1, 3, 3), "No")
        self.assertEqual(Check_Solution(1, -3, 3), "No")
        self.assertEqual(Check_Solution(1, 3, -3), "No")

    def test_boundary_cases(self):
        self.assertEqual(Check_Solution(1e-6, 3, 3), "Yes")
        self.assertEqual(Check_Solution(1, 3e-6, 3), "Yes")
        self.assertEqual(Check_Solution(1, 3, 3e-6), "Yes")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Check_Solution, "a", 3, 3)
        self.assertRaises(TypeError, Check_Solution, 1, "b", 3)
        self.assertRaises(TypeError, Check_Solution, 1, 3, "c")
