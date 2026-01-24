import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(solution(2, 3, 6), ("x = 1, y = 2"))
        self.assertEqual(solution(3, 2, 12), ("x = 2, y = 6"))
        self.assertEqual(solution(4, 2, 8), ("x = 2, y = 4"))

    def test_zero(self):
        self.assertEqual(solution(0, 0, 0), ("No solution"))

    def test_negative_numbers(self):
        self.assertEqual(solution(-2, 3, 6), ("No solution"))
        self.assertEqual(solution(-3, 2, 12), ("No solution"))
        self.assertEqual(solution(-4, 2, 8), ("No solution"))

    def test_large_numbers(self):
        self.assertEqual(solution(100, 7, 999), ("No solution"))
        self.assertEqual(solution(100, 11, 999), ("No solution"))
        self.assertEqual(solution(100, 101, 999), ("No solution"))

    def test_small_a(self):
        self.assertEqual(solution(1, 3, 6), ("No solution"))
        self.assertEqual(solution(1, 2, 12), ("No solution"))
        self.assertEqual(solution(1, 4, 8), ("No solution"))

    def test_small_b(self):
        self.assertEqual(solution(2, 1, 6), ("No solution"))
        self.assertEqual(solution(3, 1, 12), ("No solution"))
        self.assertEqual(solution(4, 1, 8), ("No solution"))
