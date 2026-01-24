import unittest
from mbpp_636_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_equal_values(self):
        self.assertEqual(Check_Solution(1, 1, 1), "Yes")

    def test_non_equal_values(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_equal_values_with_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -1, -1), "Yes")

    def test_non_equal_values_with_negative_numbers(self):
        self.assertEqual(Check_Solution(-1, -2, -3), "No")

    def test_equal_values_with_zero(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_non_equal_values_with_zero(self):
        self.assertEqual(Check_Solution(0, 1, 0), "No")
