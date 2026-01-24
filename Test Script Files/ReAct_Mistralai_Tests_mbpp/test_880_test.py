import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_two_solutions(self):
        self.assertEqual(Check_Solution(1, 3, 1), "2 solutions")
        self.assertEqual(Check_Solution(-1, 3, 1), "2 solutions")
        self.assertEqual(Check_Solution(1, -3, 1), "2 solutions")
        self.assertEqual(Check_Solution(-1, -3, 1), "2 solutions")

    def test_one_solution(self):
        self.assertEqual(Check_Solution(1, 4, -20), "1 solution")
        self.assertEqual(Check_Solution(-1, 4, -20), "1 solution")
        self.assertEqual(Check_Solution(1, -4, -20), "1 solution")
        self.assertEqual(Check_Solution(-1, -4, -20), "1 solution")

    def test_no_solutions(self):
        self.assertEqual(Check_Solution(1, 4, 2), "No solutions")
        self.assertEqual(Check_Solution(-1, 4, 2), "No solutions")
        self.assertEqual(Check_Solution(1, -4, 2), "No solutions")
        self.assertEqual(Check_Solution(-1, -4, 2), "No solutions")

    def test_zero_discriminant(self):
        self.assertEqual(Check_Solution(1, 4, 0), "1 solution")
        self.assertEqual(Check_Solution(-1, 4, 0), "1 solution")
        self.assertEqual(Check_Solution(1, -4, 0), "1 solution")
        self.assertEqual(Check_Solution(-1, -4, 0), "1 solution")

    def test_negative_coefficients(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "No solutions")
        self.assertEqual(Check_Solution(-1, 2, -3), "No solutions")
        self.assertEqual(Check_Solution(1, -2, -3), "No solutions")
        self.assertEqual(Check_Solution(1, 2, -3), "No solutions")
