import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(solution(1, 2, 5), ("x = ", 1, "y = ", 2))
        self.assertEqual(solution(2, 3, 12), ("x = ", 2, "y = ", 4))
        self.assertEqual(solution(3, 4, 12), ("x = ", 3, "y = ", 3))
        self.assertEqual(solution(4, 5, 20), ("x = ", 4, "y = ", 4))

    def test_zero_and_negative_numbers(self):
        self.assertEqual(solution(1, 2, 0), ("No solution"))
        self.assertEqual(solution(1, 2, -1), ("No solution"))
        self.assertEqual(solution(0, 2, 5), ("No solution"))
        self.assertEqual(solution(1, 0, 5), ("No solution"))

    def test_edge_cases(self):
        self.assertEqual(solution(1, 2, 1), ("No solution"))
        self.assertEqual(solution(1, 2, 2), ("x = ", 1, "y = ", 1))
        self.assertEqual(solution(1, 2, 3), ("No solution"))
        self.assertEqual(solution(1, 2, 4), ("x = ", 1, "y = ", 2))

    def test_large_numbers(self):
        self.assertEqual(solution(1000000, 1, 1000000), ("x = ", 1, "y = ", 1))
        self.assertEqual(solution(1, 1000000, 1000000), ("x = ", 999999, "y = ", 1))
        self.assertEqual(solution(1, 1, 1), ("x = ", 1, "y = ", 0))
