import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_solution1(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_solution2(self):
        self.assertEqual(solution(2, 3, 15), ("x = ", 3, ", y = ", 2))

    def test_solution3(self):
        self.assertEqual(solution(2, 3, 20), ("x = ", 4, ", y = ", 3))

    def test_solution4(self):
        self.assertEqual(solution(2, 3, 25), ("x = ", 5, ", y = ", 4))

    def test_solution5(self):
        self.assertEqual(solution(2, 3, 30), ("x = ", 5, ", y = ", 5))

    def test_solution6(self):
        self.assertEqual(solution(2, 3, 40), ("No solution"))

    def test_solution7(self):
        self.assertEqual(solution(2, 3, 50), ("No solution"))

    def test_solution8(self):
        self.assertEqual(solution(2, 3, 60), ("No solution"))
