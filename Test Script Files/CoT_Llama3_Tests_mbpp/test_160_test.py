import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_solution_typical(self):
        self.assertEqual(solution(2, 3, 12), ("x = ", 3, ", y = ", 2))

    def test_solution_edge1(self):
        self.assertEqual(solution(2, 3, 6), ("x = ", 2, ", y = ", 2))

    def test_solution_edge2(self):
        self.assertEqual(solution(2, 3, 15), ("x = ", 4, ", y = ", 3))

    def test_solution_edge3(self):
        self.assertEqual(solution(2, 3, 21), ("x = ", 5, ", y = ", 3))

    def test_solution_edge4(self):
        self.assertEqual(solution(2, 3, 24), ("x = ", 6, ", y = ", 4))

    def test_solution_edge5(self):
        self.assertEqual(solution(2, 3, 25), ("No solution"))

    def test_solution_edge6(self):
        self.assertEqual(solution(2, 3, 26), ("x = ", 6, ", y = ", 2))

    def test_solution_edge7(self):
        self.assertEqual(solution(2, 3, 27), ("No solution"))

    def test_solution_edge8(self):
        self.assertEqual(solution(2, 3, 28), ("x = ", 6, ", y = ", 4))

    def test_solution_edge9(self):
        self.assertEqual(solution(2, 3, 29), ("No solution"))

    def test_solution_edge10(self):
        self.assertEqual(solution(2, 3, 30), ("x = ", 6, ", y = ", 2))
