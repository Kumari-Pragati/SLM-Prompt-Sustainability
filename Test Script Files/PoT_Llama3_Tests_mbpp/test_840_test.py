import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 0, 2), "Yes")

    def test_edge_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case_b_nonzero(self):
        self.assertEqual(Check_Solution(1, 1, 2), "No")

    def test_edge_case_b_zero_and_c_nonzero(self):
        self.assertEqual(Check_Solution(1, 0, 4), "Yes")

    def test_edge_case_b_nonzero_and_c_zero(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No")

    def test_edge_case_b_zero_and_c_zero(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_edge_case_b_nonzero_and_c_nonzero(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")
