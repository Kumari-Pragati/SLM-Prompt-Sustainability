import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(solution(3, 4, 12), ("x = ", 1, "y = ", 3))
        self.assertEqual(solution(5, 5, 25), ("x = ", 1, "y = ", 5))
        self.assertEqual(solution(6, 8, 48), ("x = ", 2, "y = ", 7))

    def test_edge_case(self):
        self.assertEqual(solution(3, 4, 11), ("No solution"))
        self.assertEqual(solution(5, 5, 24), ("x = ", 1, "y = ", 4))
        self.assertEqual(solution(6, 8, 47), ("No solution"))

    def test_boundary_case(self):
        self.assertEqual(solution(3, 4, 12), ("x = ", 1, "y = ", 3))
        self.assertEqual(solution(3, 4, 13), ("No solution"))
        self.assertEqual(solution(5, 5, 25), ("x = ", 1, "y = ", 5))
        self.assertEqual(solution(5, 5, 26), ("No solution"))
        self.assertEqual(solution(6, 8, 48), ("x = ", 2, "y = ", 7))
        self.assertEqual(solution(6, 8, 49), ("No solution"))
