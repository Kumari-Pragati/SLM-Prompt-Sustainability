import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")

    def test_typical_case_2(self):
        self.assertEqual(Check_Solution(10, 10, 10), "Yes")

    def test_edge_case_a_equals_c(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_case_a_not_equals_c(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -2, -1), "Yes")

    def test_large_numbers(self):
        self.assertEqual(Check_Solution(1000000, 1000000, 1000000), "Yes")

    def test_zero_and_non_zero(self):
        self.assertEqual(Check_Solution(0, 1, 0), "No")
