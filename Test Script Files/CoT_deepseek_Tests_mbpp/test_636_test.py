import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")

    def test_edge_case(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_boundary_case(self):
        self.assertEqual(Check_Solution(1000, 1000, 1000), "Yes")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")
