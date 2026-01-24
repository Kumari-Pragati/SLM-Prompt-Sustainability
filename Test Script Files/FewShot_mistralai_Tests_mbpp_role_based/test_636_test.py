import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_different_numbers(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "No")

    def test_mixed_numbers(self):
        self.assertEqual(Check_Solution(1, -2, 1), "No")

    def test_invalid_input(self):
        self.assertRaises(TypeError, Check_Solution, "a", "b", "c")
