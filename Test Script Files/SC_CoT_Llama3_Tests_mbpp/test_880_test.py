import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_two_solutions(self):
        self.assertEqual(Check_Solution(1, 2, 3), "2 solutions")

    def test_one_solution(self):
        self.assertEqual(Check_Solution(1, 0, 1), "1 solution")

    def test_no_solutions(self):
        self.assertEqual(Check_Solution(1, 0, 0), "No solutions")

    def test_zero_discriminant(self):
        self.assertEqual(Check_Solution(0, 0, 1), "1 solution")

    def test_negative_discriminant(self):
        self.assertEqual(Check_Solution(1, -2, 3), "No solutions")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            Check_Solution(1, 2, "c")
