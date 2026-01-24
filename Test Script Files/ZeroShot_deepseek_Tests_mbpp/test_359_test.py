import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(Check_Solution(1, 2, -3), "Yes")
        self.assertEqual(Check_Solution(1, 4, -12), "Yes")
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -2, 3), "Yes")
        self.assertEqual(Check_Solution(-1, -4, 12), "Yes")
        self.assertEqual(Check_Solution(-1, 0, 0), "Yes")

    def test_mixed_numbers(self):
        self.assertEqual(Check_Solution(-1, 2, 3), "No")
        self.assertEqual(Check_Solution(1, -4, 12), "No")
        self.assertEqual(Check_Solution(1, 0, -1), "No")

    def test_zero_coefficients(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(0, 2, 0), "Yes")
        self.assertEqual(Check_Solution(0, -2, 0), "Yes")
