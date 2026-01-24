import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_boundary_condition(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_edge_case(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 1)
