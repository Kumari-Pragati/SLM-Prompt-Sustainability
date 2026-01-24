import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_simple_same(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_simple_different(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_edge_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_edge_min_positive(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_edge_max_positive(self):
        self.assertEqual(Check_Solution(2147483647, 2147483647, 2147483647), "Yes")

    def test_edge_negative(self):
        self.assertEqual(Check_Solution(-1, -1, -1), "Yes")

    def test_edge_min_negative(self):
        self.assertEqual(Check_Solution(-2147483648, -2147483648, -2147483648), "Yes")

    def test_edge_zero_mixed(self):
        self.assertEqual(Check_Solution(0, 1, 0), "Yes")

    def test_edge_max_mixed(self):
        self.assertEqual(Check_Solution(2147483647, 2147483648, 2147483647), "No")
