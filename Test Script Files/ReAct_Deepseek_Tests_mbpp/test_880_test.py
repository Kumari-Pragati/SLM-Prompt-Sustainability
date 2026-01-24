import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(Check_Solution(1, -3, 2), "2 solutions")

    def test_zero_discriminant(self):
        self.assertEqual(Check_Solution(1, -2, 1), "1 solution")

    def test_negative_discriminant(self):
        self.assertEqual(Check_Solution(1, -1, 1), "No solutions")

    def test_zero_coefficients(self):
        self.assertEqual(Check_Solution(0, 0, 0), "No solutions")

    def test_negative_coefficients(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "2 solutions")

    def test_negative_a(self):
        self.assertEqual(Check_Solution(-1, 2, 1), "2 solutions")

    def test_zero_a(self):
        self.assertRaises(ValueError, Check_Solution, 0, 1, 1)
