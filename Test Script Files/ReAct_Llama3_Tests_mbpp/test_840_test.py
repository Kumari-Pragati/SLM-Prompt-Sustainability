import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case_b_nonzero(self):
        self.assertEqual(Check_Solution(1, 1, 3), "No")

    def test_edge_case_b_negative(self):
        self.assertEqual(Check_Solution(1, -1, 3), "No")

    def test_edge_case_b_zero_and_c_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_case_b_zero_and_c_nonzero(self):
        self.assertEqual(Check_Solution(0, 0, 1), "Yes")
