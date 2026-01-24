import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(Check_Solution(1, 3, 3), "Yes")
        self.assertEqual(Check_Solution(2, 4, 2), "Yes")
        self.assertEqual(Check_Solution(3, 6, 1), "Yes")

    def test_zero_and_negative_numbers(self):
        self.assertNotEqual(Check_Solution(0, 3, 3), "Yes")
        self.assertNotEqual(Check_Solution(-1, 3, 3), "Yes")
        self.assertNotEqual(Check_Solution(1, 0, 3), "Yes")
        self.assertNotEqual(Check_Solution(1, -3, 3), "Yes")
        self.assertNotEqual(Check_Solution(1, 3, 0), "Yes")
        self.assertNotEqual(Check_Solution(1, 3, -3), "Yes")

    def test_non_integer_values(self):
        self.assertNotEqual(Check_Solution(1.1, 3, 3), "Yes")
        self.assertNotEqual(Check_Solution(1, 3.1, 3), "Yes")
        self.assertNotEqual(Check_Solution(1, 3, 3.1), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(1, 3, 1), "No")
        self.assertEqual(Check_Solution(1, 3, 2), "No")
        self.assertEqual(Check_Solution(1, 3, 3), "No")
        self.assertEqual(Check_Solution(1, 4, 3), "No")
        self.assertEqual(Check_Solution(2, 3, 1), "No")
        self.assertEqual(Check_Solution(2, 3, 2), "No")
        self.assertEqual(Check_Solution(2, 3, 3), "No")
        self.assertEqual(Check_Solution(2, 4, 3), "No")
