import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_positive_delta(self):
        self.assertEqual(Check_Solution(1, 2, 3), "2 solutions")

    def test_zero_delta(self):
        self.assertEqual(Check_Solution(1, 0, 1), "1 solution")

    def test_negative_delta(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No solutions")

    def test_zero_coefficient(self):
        self.assertEqual(Check_Solution(0, 0, 1), "No solutions")

    def test_zero_a(self):
        self.assertEqual(Check_Solution(0, 0, 0), "No solutions")

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")
