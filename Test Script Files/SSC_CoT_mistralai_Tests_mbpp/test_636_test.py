import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")
        self.assertEqual(Check_Solution(-3, -3, -3), "Yes")

    def test_edge_case(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")
        self.assertEqual(Check_Solution(1, 1, 0), "Yes")

    def test_boundary_case(self):
        self.assertEqual(Check_Solution(sys.maxsize, sys.maxsize, sys.maxsize), "Yes")
        self.assertEqual(Check_Solution(-sys.maxsize, -sys.maxsize, -sys.maxsize), "Yes")

    def test_invalid_input(self):
        self.assertIsNone(Check_Solution(1, "a", 1))
        self.assertIsNone(Check_Solution(1, 2, "a"))
        self.assertIsNone(Check_Solution("a", 2, 1))
