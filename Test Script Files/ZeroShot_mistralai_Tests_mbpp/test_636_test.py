import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_equal_sides(self):
        self.assertEqual(Check_Solution(3, 3, 3), "Yes")
        self.assertEqual(Check_Solution(4, 4, 4), "Yes")
        self.assertEqual(Check_Solution(5, 5, 5), "Yes")

    def test_different_sides(self):
        self.assertEqual(Check_Solution(3, 4, 5), "No")
        self.assertEqual(Check_Solution(4, 5, 6), "No")
        self.assertEqual(Check_Solution(5, 6, 7), "No")
