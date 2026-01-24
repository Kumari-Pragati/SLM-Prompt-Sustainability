import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(solution(3, 2, 10), ("x = ", 3, ", y = ", 1))

    def test_boundary_conditions(self):
        self.assertEqual(solution(1, 1, 0), ("x = ", 0, ", y = ", 0))
        self.assertEqual(solution(1, 1, 1), ("x = ", 1, ", y = ", 1))

    def test_edge_cases(self):
        self.assertEqual(solution(2, 3, 10), ("No solution"))
        self.assertEqual(solution(0, 1, 10), ("No solution"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            solution("a", 2, 10)
        with self.assertRaises(TypeError):
            solution(2, "b", 10)
        with self.assertRaises(TypeError):
            solution(2, 3, "n")
        with self.assertRaises(ValueError):
            solution(-1, 2, 10)
        with self.assertRaises(ValueError):
            solution(2, -1, 10)
        with self.assertRaises(ValueError):
            solution(2, 3, -10)
