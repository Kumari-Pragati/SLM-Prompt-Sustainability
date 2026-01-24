import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_check_solution_positive_two_solutions(self):
        self.assertEqual(Check_Solution(1, 4, 1), "2 solutions")
        self.assertEqual(Check_Solution(4, 16, 1), "2 solutions")
        self.assertEqual(Check_Solution(9, 81, 4), "2 solutions")

    def test_check_solution_positive_one_solution(self):
        self.assertEqual(Check_Solution(1, 1, 1), "1 solution")
        self.assertEqual(Check_Solution(4, 16, 25), "1 solution")
        self.assertEqual(Check_Solution(9, 81, 81), "1 solution")

    def test_check_solution_no_solutions(self):
        self.assertEqual(Check_Solution(1, 4, 5), "No solutions")
        self.assertEqual(Check_Solution(4, 16, 26), "No solutions")
        self.assertEqual(Check_Solution(9, 81, 82), "No solutions")
