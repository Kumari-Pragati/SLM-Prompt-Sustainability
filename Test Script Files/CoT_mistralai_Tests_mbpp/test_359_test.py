import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(Check_Solution(1, 3, 3), "Yes")
        self.assertEqual(Check_Solution(2, 4, 2), "Yes")
        self.assertEqual(Check_Solution(3, 9, 1), "Yes")

    def test_negative(self):
        self.assertEqual(Check_Solution(1, 3, 2), "No")
        self.assertEqual(Check_Solution(2, 4, 3), "No")
        self.assertEqual(Check_Solution(3, 9, 2), "No")

    def test_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "No")
        self.assertEqual(Check_Solution(0, 3, 0), "No")
        self.assertEqual(Check_Solution(3, 0, 0), "No")

    def test_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -3, -3), "No")
        self.assertEqual(Check_Solution(-2, -4, -2), "No")
        self.assertEqual(Check_Solution(-3, -9, -1), "No")

    def test_floats(self):
        self.assertEqual(Check_Solution(1.1, 3.3, 3.3), "No")
        self.assertEqual(Check_Solution(2.2, 4.4, 2.2), "No")
        self.assertEqual(Check_Solution(3.3, 9.9, 1.1), "No")
