import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_division_by_zero(self):
        self.assertEqual(Check_Solution(1, 0, 2), "Yes")

    def test_division_by_nonzero(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_zero_divided_by_zero(self):
        self.assertEqual(Check_Solution(0, 0, 4), "Yes")

    def test_negative_division(self):
        self.assertEqual(Check_Solution(-1, 2, 3), "No")

    def test_zero_division(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
