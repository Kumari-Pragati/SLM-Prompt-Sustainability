import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_simple_negative(self):
        self.assertEqual(Check_Solution(-1, 2, -3), "No")

    def test_zero_b(self):
        self.assertEqual(Check_Solution(0, 0, 1), "Yes")

    def test_edge_cases_a(self):
        self.assertEqual(Check_Solution(sys.maxsize, 1, 1), "No")
        self.assertEqual(Check_Solution(-sys.maxsize, 1, 1), "No")

    def test_edge_cases_b(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")
        self.assertEqual(Check_Solution(1, 0, -1), "No")

    def test_edge_cases_c(self):
        self.assertEqual(Check_Solution(1, 1, 0), "Yes")
        self.assertEqual(Check_Solution(1, -1, 0), "No")
