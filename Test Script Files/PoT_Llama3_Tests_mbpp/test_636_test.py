import unittest
from mbpp_636_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_case_a_eq_c(self):
        self.assertEqual(Check_Solution(2, 2, 2), "Yes")

    def test_edge_case_b_eq_c(self):
        self.assertEqual(Check_Solution(1, 2, 2), "No")

    def test_edge_case_a_eq_b(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_case_c_eq_zero(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No")

    def test_edge_case_c_eq_negative(self):
        self.assertEqual(Check_Solution(1, 2, -1), "No")

    def test_edge_case_a_eq_zero(self):
        self.assertEqual(Check_Solution(0, 2, 0), "Yes")

    def test_edge_case_b_eq_zero(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_edge_case_a_eq_negative(self):
        self.assertEqual(Check_Solution(-1, 2, -1), "No")

    def test_edge_case_b_eq_negative(self):
        self.assertEqual(Check_Solution(1, -1, -1), "No")
