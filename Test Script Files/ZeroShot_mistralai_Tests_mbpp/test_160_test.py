import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_solution_simple_case(self):
        self.assertEqual(solution(2, 3, 6), ("x = 1, y = 2"))
        self.assertEqual(solution(3, 4, 12), ("x = 3, y = 4"))
        self.assertEqual(solution(5, 6, 30), ("x = 5, y = 6"))

    def test_solution_negative_case(self):
        self.assertEqual(solution(2, 3, 5), "No solution")
        self.assertEqual(solution(3, 4, 7), "No solution")
        self.assertEqual(solution(5, 6, 29), "No solution")

    def test_solution_edge_case(self):
        self.assertEqual(solution(2, 3, 7), "No solution")
        self.assertEqual(solution(3, 4, 11), "No solution")
        self.assertEqual(solution(5, 6, 28), "No solution")
