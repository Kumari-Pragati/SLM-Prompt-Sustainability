import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_boundary_conditions(self):
        self.assertEqual(solution(1, 1, 0), ("x = ", 0, ", y = ", 0))
        self.assertEqual(solution(1, 1, 1), ("x = ", 1, ", y = ", 0))

    def test_edge_cases(self):
        self.assertEqual(solution(1, 2, 3), "No solution")
        self.assertEqual(solution(2, 3, 4), ("x = ", 1, ", y = ", 0))
        self.assertEqual(solution(3, 4, 5), "No solution")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            solution("a", 2, 3)
        with self.assertRaises(TypeError):
            solution(2, "b", 3)
        with self.assertRaises(TypeError):
            solution(2, 3, "c")
