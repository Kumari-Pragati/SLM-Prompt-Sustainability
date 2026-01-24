import unittest
from mbpp_636_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")
        self.assertEqual(Check_Solution(2, 2, 2), "Yes")
        self.assertEqual(Check_Solution(3, 3, 3), "Yes")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(-1, -1, -1), "Yes")
        self.assertEqual(Check_Solution(1, 2, 1), "No")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 1)
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")
