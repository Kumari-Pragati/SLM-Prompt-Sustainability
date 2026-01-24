import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_edge_case_a_zero(self):
        self.assertEqual(solution(0, 3, 10), ("x = ", 0, ", y = ", 10))

    def test_edge_case_b_zero(self):
        self.assertEqual(solution(2, 0, 10), ("No solution"))

    def test_edge_case_n_zero(self):
        self.assertEqual(solution(2, 3, 0), ("No solution"))

    def test_edge_case_a_negative(self):
        self.assertEqual(solution(-2, 3, 10), ("No solution"))

    def test_edge_case_b_negative(self):
        self.assertEqual(solution(2, -3, 10), ("No solution"))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            solution("a", 3, 10)
