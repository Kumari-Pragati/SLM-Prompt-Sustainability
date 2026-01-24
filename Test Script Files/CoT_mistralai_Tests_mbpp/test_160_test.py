import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(solution(2, 3, 12), ("x = ", 3, "y = ", 4))
        self.assertEqual(solution(3, 4, 24), ("x = ", 2, "y = ", 6))

    def test_edge_case(self):
        self.assertEqual(solution(2, 3, 11), ("No solution"))
        self.assertEqual(solution(3, 4, 23), ("No solution"))

    def test_boundary_case(self):
        self.assertEqual(solution(2, 3, 0), ("No solution"))
        self.assertEqual(solution(2, 3, 1), ("No solution"))
        self.assertEqual(solution(2, 3, 1200000000), ("No solution"))

    def test_invalid_input(self):
        self.assertRaises(TypeError, solution, "a", 3, 12)
        self.assertRaises(TypeError, solution, 2, "b", 12)
        self.assertRaises(TypeError, solution, 2, 3, "n")
