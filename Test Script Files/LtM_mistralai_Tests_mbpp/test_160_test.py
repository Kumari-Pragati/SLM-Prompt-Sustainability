import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(solution(1, 2, 5), ("x = 1, y = 3"))
        self.assertEqual(solution(2, 3, 12), ("x = 2, y = 4"))
        self.assertEqual(solution(3, 4, 12), ("No solution"))

    def test_edge_cases(self):
        self.assertEqual(solution(1, 2, 1), ("No solution"))
        self.assertEqual(solution(1, 2, 2), ("x = 1, y = 1"))
        self.assertEqual(solution(1, 2, 3), ("No solution"))

    def test_complex(self):
        self.assertEqual(solution(10, 3, 30), ("x = 3, y = 10"))
        self.assertEqual(solution(10, 3, 31), ("No solution"))
        self.assertEqual(solution(10, 3, 32), ("x = 2, y = 11"))
