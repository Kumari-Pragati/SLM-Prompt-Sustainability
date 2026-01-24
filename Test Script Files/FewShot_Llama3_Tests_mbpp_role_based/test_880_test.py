import unittest
from mbpp_880_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_two_solutions(self):
        self.assertEqual(Check_Solution(1, 2, 3), "2 solutions")

    def test_one_solution(self):
        self.assertEqual(Check_Solution(1, 2, 1), "1 solution")

    def test_no_solutions(self):
        self.assertEqual(Check_Solution(1, 0, 1), "No solutions")

    def test_zero_coefficient(self):
        self.assertEqual(Check_Solution(0, 2, 3), "1 solution")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 2, 3)
