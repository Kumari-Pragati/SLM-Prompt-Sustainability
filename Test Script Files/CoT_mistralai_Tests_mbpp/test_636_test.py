import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_equal_sides(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")
        self.assertEqual(Check_Solution(-1, -1, -1), "Yes")
        self.assertEqual(Check_Solution(3.14, 3.14, 3.14), "Yes")

    def test_different_sides(self):
        self.assertEqual(Check_Solution(1, 1, 2), "No")
        self.assertEqual(Check_Solution(-1, -1, 1), "No")
        self.assertEqual(Check_Solution(3.14, 2.71, 4.14), "No")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Check_Solution, "a", 1, 1)
        self.assertRaises(TypeError, Check_Solution, 1, "b", 1)
        self.assertRaises(TypeError, Check_Solution, 1, 1, "c")
        self.assertRaises(TypeError, Check_Solution, 1, 1, None)
