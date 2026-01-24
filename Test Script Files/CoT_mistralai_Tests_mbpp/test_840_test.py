import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")
        self.assertEqual(Check_Solution(-1, 2, 3), "No")
        self.assertEqual(Check_Solution(1, -2, 3), "No")
        self.assertEqual(Check_Solution(1, 2, -3), "No")
        self.assertEqual(Check_Solution(-1, -2, -3), "No")

    def test_zero_division(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")
        self.assertEqual(Check_Solution(1, 0, -3), "Yes")
        self.assertEqual(Check_Solution(-1, 0, 3), "Yes")
        self.assertEqual(Check_Solution(-1, 0, -3), "Yes")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Check_Solution, "a", 1, 2)
        self.assertRaises(TypeError, Check_Solution, 1, "b", 2)
        self.assertRaises(TypeError, Check_Solution, 1, 2, "c")
