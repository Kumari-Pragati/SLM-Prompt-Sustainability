import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_solution_with_valid_input(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))
        self.assertEqual(solution(3, 4, 12), ("x = ", 1, ", y = ", 1))
        self.assertEqual(solution(5, 6, 30), ("x = ", 3, ", y = ", 2))

    def test_solution_with_no_solution(self):
        self.assertEqual(solution(2, 3, 5), "No solution")
        self.assertEqual(solution(3, 4, 10), "No solution")
        self.assertEqual(solution(5, 6, 20), "No solution")

    def test_solution_with_zero_input(self):
        self.assertEqual(solution(0, 3, 10), "No solution")
        self.assertEqual(solution(3, 0, 12), "No solution")
        self.assertEqual(solution(0, 0, 20), "No solution")
