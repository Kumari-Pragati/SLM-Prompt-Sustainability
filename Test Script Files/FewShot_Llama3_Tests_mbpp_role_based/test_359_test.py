import unittest
from mbpp_359_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_valid_solution(self):
        self.assertEqual(Check_Solution(1, 3, 2), "Yes")

    def test_invalid_solution(self):
        self.assertEqual(Check_Solution(2, 3, 4), "No")

    def test_zero_coefficient(self):
        self.assertEqual(Check_Solution(0, 3, 2), "No")

    def test_zero_constant(self):
        self.assertEqual(Check_Solution(1, 0, 2), "No")

    def test_zero_coefficient_and_constant(self):
        self.assertEqual(Check_Solution(0, 0, 2), "No")
