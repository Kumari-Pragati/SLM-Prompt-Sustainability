import unittest
from mbpp_636_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(3, 4, 3), "Yes")
        self.assertEqual(Check_Solution(5, 6, 5), "Yes")

    def test_edge_cases(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(3, 4, 3), "Yes")
        self.assertEqual(Check_Solution(5, 6, 5), "Yes")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 2, 3)
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")

    def test_boundary_conditions(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(3, 4, 3), "Yes")
        self.assertEqual(Check_Solution(5, 6, 5), "Yes")
