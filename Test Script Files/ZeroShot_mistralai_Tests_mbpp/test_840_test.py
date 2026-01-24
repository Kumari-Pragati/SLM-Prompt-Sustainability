import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_check_solution_divisible_by_b(self):
        self.assertEqual(Check_Solution(3, 3, 9), "Yes")
        self.assertEqual(Check_Solution(12, 4, 48), "Yes")

    def test_check_solution_not_divisible_by_b(self):
        self.assertEqual(Check_Solution(3, 2, 4), "No")
        self.assertEqual(Check_Solution(10, 5, 25), "No")
