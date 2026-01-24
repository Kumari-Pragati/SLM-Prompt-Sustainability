import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_not_equal(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_equal_again(self):
        self.assertEqual(Check_Solution(4, 4, 4), "Yes")

    def test_not_equal_again(self):
        self.assertEqual(Check_Solution(5, 6, 7), "No")
