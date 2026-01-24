import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_b_is_zero(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_b_is_not_zero(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")
