import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")
        self.assertEqual(Check_Solution(4, 0, 5), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(1, 1, 3), "No")
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 3)
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)
        with self.assertRaises(TypeError):
            Check_Solution(1, 0, "c")

    def test_boundary_cases(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1, 0, -1), "Yes")
