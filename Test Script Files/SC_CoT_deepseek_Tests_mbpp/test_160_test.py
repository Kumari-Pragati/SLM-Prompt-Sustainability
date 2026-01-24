import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(solution(3, 2, 10), ("x = ", 3, ", y = ", 1))

    def test_boundary_case(self):
        self.assertEqual(solution(1, 1, 1), ("x = ", 1, ", y = ", 1))

    def test_edge_case(self):
        self.assertEqual(solution(0, 1, 0), ("x = ", 0, ", y = ", 0))
        self.assertEqual(solution(1, 0, 1), ("No solution"))
        self.assertEqual(solution(0, 0, 0), ("No solution"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            solution("a", 1, 1)
        with self.assertRaises(TypeError):
            solution(1, "b", 1)
        with self.assertRaises(TypeError):
            solution(1, 1, "c")
        with self.assertRaises(ValueError):
            solution(-1, 1, 1)
        with self.assertRaises(ValueError):
            solution(1, -1, 1)
        with self.assertRaises(ValueError):
            solution(1, 1, -1)
