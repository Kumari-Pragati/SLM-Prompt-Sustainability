import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_equal_values(self):
        self.assertEqual(Check_Solution(1, 2, 1), "Yes")

    def test_unequal_values(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_zero_values(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_negative_values(self):
        self.assertEqual(Check_Solution(-1, -2, -1), "Yes")

    def test_mixed_values(self):
        self.assertEqual(Check_Solution(-1, 2, -1), "No")
