import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_two_solutions(self):
        self.assertEqual(Check_Solution(1, 3, 1), "2 solutions")
        self.assertEqual(Check_Solution(1, 9, 4), "2 solutions")

    def test_one_solution(self):
        self.assertEqual(Check_Solution(1, 4, 1), "1 solution")
        self.assertEqual(Check_Solution(-1, 4, 4), "1 solution")

    def test_no_solutions(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No solutions")
        self.assertEqual(Check_Solution(-1, -1, 1), "No solutions")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Check_Solution, "a", "b", "c")
        self.assertRaises(TypeError, Check_Solution, 1, "b", "c")
        self.assertRaises(TypeError, Check_Solution, 1, 1, "c")
