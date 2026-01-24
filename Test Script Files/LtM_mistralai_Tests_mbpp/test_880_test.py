import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_positive_solutions(self):
        self.assertEqual(Check_Solution(1, 4, 1), "2 solutions")
        self.assertEqual(Check_Solution(1, 1, 1), "2 solutions")
        self.assertEqual(Check_Solution(1, 9, 4), "2 solutions")

    def test_simple_one_solution(self):
        self.assertEqual(Check_Solution(1, 4, 0), "1 solution")
        self.assertEqual(Check_Solution(1, 1, 0), "1 solution")
        self.assertEqual(Check_Solution(1, 4, -4), "1 solution")

    def test_simple_no_solutions(self):
        self.assertEqual(Check_Solution(1, 4, 5), "No solutions")
        self.assertEqual(Check_Solution(1, 1, 2), "No solutions")
        self.assertEqual(Check_Solution(1, -1, 1), "No solutions")

    def test_negative_coefficients(self):
        self.assertEqual(Check_Solution(-1, 4, 1), "2 solutions")
        self.assertEqual(Check_Solution(-1, -4, 1), "2 solutions")
        self.assertEqual(Check_Solution(-1, 4, -1), "No solutions")

    def test_zero_coefficients(self):
        self.assertEqual(Check_Solution(0, 4, 1), "1 solution")
        self.assertEqual(Check_Solution(0, 0, 0), "1 solution")
        self.assertEqual(Check_Solution(0, 4, 0), "1 solution")
