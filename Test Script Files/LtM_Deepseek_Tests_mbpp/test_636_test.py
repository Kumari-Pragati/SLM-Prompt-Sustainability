import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")

    def test_edge_case_equal_values(self):
        self.assertEqual(Check_Solution(5, 5, 5), "Yes")

    def test_edge_case_different_values(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_edge_case_zero_values(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_case_negative_values(self):
        self.assertEqual(Check_Solution(-1, -2, -1), "Yes")

    def test_edge_case_large_values(self):
        self.assertEqual(Check_Solution(1000000, 1000000, 1000000), "Yes")
