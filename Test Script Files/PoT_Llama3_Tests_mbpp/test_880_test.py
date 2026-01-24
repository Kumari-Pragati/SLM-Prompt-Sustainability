import unittest
from mbpp_880_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No solutions")

    def test_edge_case_a_zero(self):
        self.assertEqual(Check_Solution(0, 2, 3), "1 solution")

    def test_edge_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 3), "No solutions")

    def test_edge_case_c_zero(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No solutions")

    def test_edge_case_b_squared_four_a_c(self):
        self.assertEqual(Check_Solution(1, 2, 1), "2 solutions")

    def test_edge_case_b_squared_four_a_c_equal_zero(self):
        self.assertEqual(Check_Solution(1, 0, 1), "1 solution")

    def test_edge_case_b_squared_four_a_c_negative(self):
        self.assertEqual(Check_Solution(1, 2, -1), "No solutions")
