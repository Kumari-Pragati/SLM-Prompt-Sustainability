import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(Check_Solution(1, 3, 2), "Yes")
        self.assertEqual(Check_Solution(2, 4, 1), "Yes")
        self.assertEqual(Check_Solution(3, 5, 2), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")
        self.assertEqual(Check_Solution(2, 2, 2), "Yes")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 1, 2)
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 2)
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")

    def test_special_cases(self):
        self.assertEqual(Check_Solution(-1, 1, 1), "Yes")
        self.assertEqual(Check_Solution(1, -1, 1), "Yes")
        self.assertEqual(Check_Solution(1, 1, -1), "No")
