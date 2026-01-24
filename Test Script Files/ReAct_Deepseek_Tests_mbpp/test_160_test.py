import unittest
from mbpp_160_code import solution

class TestSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(solution(2, 3, 10), ("x = ", 2, ", y = ", 1))

    def test_boundary_case(self):
        self.assertEqual(solution(1, 1, 0), ("x = ", 0, ", y = ", 0))

    def test_no_solution(self):
        self.assertEqual(solution(3, 4, 1), "No solution")

    def test_negative_values(self):
        self.assertEqual(solution(-2, -3, -10), ("x = ", -2, ", y = ", -1))

    def test_zero_values(self):
        self.assertEqual(solution(0, 0, 0), "No solution")

    def test_large_numbers(self):
        self.assertEqual(solution(1000, 2000, 3000000), ("x = ", 3000, ", y = ", 1500))
