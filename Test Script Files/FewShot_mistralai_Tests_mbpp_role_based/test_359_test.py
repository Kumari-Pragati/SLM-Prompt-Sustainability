import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(Check_Solution(1, 2, 3), "Yes")
        self.assertEqual(Check_Solution(2, 3, 4), "Yes")
        self.assertEqual(Check_Solution(3, 4, 5), "Yes")

    def test_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "No")
        self.assertEqual(Check_Solution(0, 2, 0), "No")
        self.assertEqual(Check_Solution(2, 0, 0), "No")

    def test_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "No")
        self.assertEqual(Check_Solution(-2, -3, -4), "No")
        self.assertEqual(Check_Solution(-3, -4, -5), "No")

    def test_mixed_numbers(self):
        self.assertEqual(Check_Solution(1, -2, 3), "No")
        self.assertEqual(Check_Solution(-1, 2, -3), "No")
        self.assertEqual(Check_Solution(-1, -2, 2), "No")

    def test_edge_case_1(self):
        self.assertEqual(Check_Solution(1, 3, 3), "Yes")

    def test_edge_case_2(self):
        self.assertEqual(Check_Solution(2, 4, 2), "Yes")

    def test_edge_case_3(self):
        self.assertEqual(Check_Solution(3, 5, 1.5), "No")
