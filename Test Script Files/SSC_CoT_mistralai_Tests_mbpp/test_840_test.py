import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_zero_case(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
        self.assertEqual(Check_Solution(-1, 0, 0), "Yes")

    def test_non_zero_case(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")
        self.assertEqual(Check_Solution(-1, -1, -1), "No")
        self.assertEqual(Check_Solution(1, -1, 1), "No")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(0, 1, 0), "No")
        self.assertEqual(Check_Solution(0, -1, 0), "No")
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
        self.assertEqual(Check_Solution(-1, 0, 0), "Yes")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Check_Solution, "a", "b", "c")
        self.assertRaises(TypeError, Check_Solution, 1, "b", 1)
        self.assertRaises(TypeError, Check_Solution, 1, 1, "c")
