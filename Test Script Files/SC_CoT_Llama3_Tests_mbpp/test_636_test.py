import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")
        self.assertEqual(Check_Solution(2, 2, 2), "Yes")
        self.assertEqual(Check_Solution(3, 3, 3), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(1, 2, 1), "No")
        self.assertEqual(Check_Solution(1, 1, 2), "No")
        self.assertEqual(Check_Solution(1, 2, 3), "No")
        self.assertEqual(Check_Solution(2, 1, 1), "No")
        self.assertEqual(Check_Solution(2, 2, 3), "No")
        self.assertEqual(Check_Solution(3, 1, 1), "No")
        self.assertEqual(Check_Solution(3, 2, 2), "No")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 1, 1)
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 1)
        with self.assertRaises(TypeError):
            Check_Solution(1, 1, "c")
