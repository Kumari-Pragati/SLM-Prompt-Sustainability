import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))
        self.assertEqual(solution(3, 5, 15), ("x = ", 1, ", y = ", 1))

    def test_edge_conditions(self):
        self.assertEqual(solution(1, 1, 0), ("x = ", 0, ", y = ", 0))
        self.assertEqual(solution(0, 1, 10), "No solution")
        self.assertEqual(solution(1, 0, 10), "No solution")

    def test_boundary_conditions(self):
        self.assertEqual(solution(1, 1, 10**9), ("x = ", 10**9, ", y = ", 10**9))
        self.assertEqual(solution(10**9, 1, 1), ("x = ", 0, ", y = ", 0))

    def test_complex_cases(self):
        self.assertEqual(solution(4, 6, 24), ("x = ", 3, ", y = ", 2))
        self.assertEqual(solution(5, 7, 35), ("x = ", 5, ", y = ", 1))
