import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_check_solution_positive(self):
        self.assertEqual(Check_Solution(1, 3, 4), "Yes")
        self.assertEqual(Check_Solution(2, 6, 3), "Yes")
        self.assertEqual(Check_Solution(3, 9, 2), "Yes")

    def test_check_solution_negative(self):
        self.assertNotEqual(Check_Solution(1, 2, 3), "Yes")
        self.assertNotEqual(Check_Solution(2, 4, 5), "Yes")
        self.assertNotEqual(Check_Solution(3, 7, 2), "Yes")
