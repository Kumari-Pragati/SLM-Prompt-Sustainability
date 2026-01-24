import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(solution(2, 3, 12), ("x = ", 3, "y = ", 4))
        self.assertEqual(solution(3, 4, 24), ("x = ", 2, "y = ", 6))

    def test_edge_cases(self):
        self.assertEqual(solution(2, 3, 11), ("No solution"))
        self.assertEqual(solution(3, 4, 23), ("No solution"))
        self.assertEqual(solution(2, 3, 0), ("No solution"))
        self.assertEqual(solution(3, 4, -1), ("No solution"))

    def test_boundary_cases(self):
        self.assertEqual(solution(2, 3, 1), ("No solution"))
        self.assertEqual(solution(2, 3, 13), ("x = ", 6, "y = ", 5))
        self.assertEqual(solution(3, 4, 22), ("x = ", 5, "y = ", 6))
        self.assertEqual(solution(3, 4, 25), ("No solution"))
