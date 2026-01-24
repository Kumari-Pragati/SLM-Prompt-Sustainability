import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_boundary_condition(self):
        self.assertEqual(solution(1, 1, 0), ("x = ", 0, ", y = ", 0))

    def test_edge_condition(self):
        self.assertEqual(solution(1, 2, 1), ("No solution"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            solution("a", 2, 3)
