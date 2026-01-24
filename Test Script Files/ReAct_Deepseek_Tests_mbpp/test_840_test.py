import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_b_equals_zero(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_b_not_zero(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_negative_values(self):
        self.assertEqual(Check_Solution(-1, 0, -1), "Yes")

    def test_zero_values(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_large_numbers(self):
        self.assertEqual(Check_Solution(1000, 0, 1000), "Yes")

    def test_b_not_zero_large_numbers(self):
        self.assertEqual(Check_Solution(1000, 1, 1000), "No")
