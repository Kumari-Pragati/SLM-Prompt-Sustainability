import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_zero_division(self):
        """Test if function correctly returns 'Yes' for zero divisor."""
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_non_zero_division(self):
        """Test if function correctly returns 'No' for non-zero divisor."""
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_negative_numbers(self):
        """Test if function correctly handles negative numbers."""
        self.assertEqual(Check_Solution(-1, -1, -1), "No")
        self.assertEqual(Check_Solution(-1, 0, -1), "Yes")

    def test_zero_and_non_zero(self):
        """Test if function correctly handles zero and non-zero values."""
        self.assertEqual(Check_Solution(0, 1, 0), "Yes")
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")
        self.assertEqual(Check_Solution(0, 0, 1), "Yes")

    def test_invalid_input(self):
        """Test if function correctly handles invalid inputs."""
        self.assertRaises(TypeError, Check_Solution, "a", "b", "c")
        self.assertRaises(TypeError, Check_Solution, 1, "b", 1)
        self.assertRaises(TypeError, Check_Solution, 1, 1, "c")
