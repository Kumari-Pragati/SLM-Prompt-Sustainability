import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(solution(2, 3, 12), ("x = ", 3, ", y = ", 3))

    def test_edge_case_a_zero(self):
        self.assertEqual(solution(0, 3, 12), ("x = ", 0, ", y = ", 4))

    def test_edge_case_b_zero(self):
        self.assertEqual(solution(2, 0, 12), ("No solution"))

    def test_edge_case_n_zero(self):
        self.assertEqual(solution(2, 3, 0), ("No solution"))

    def test_edge_case_n_negative(self):
        self.assertEqual(solution(2, 3, -12), ("No solution"))

    def test_edge_case_a_negative(self):
        self.assertEqual(solution(-2, 3, 12), ("No solution"))

    def test_edge_case_b_negative(self):
        self.assertEqual(solution(2, -3, 12), ("No solution"))

    def test_edge_case_all_zero(self):
        self.assertEqual(solution(0, 0, 0), ("No solution"))
