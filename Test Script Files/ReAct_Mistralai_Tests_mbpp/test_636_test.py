import unittest
from mbpp_636_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_same_numbers(self):
        """Test if function returns 'Yes' when a, b, and c are the same."""
        self.assertEqual(Check_Solution(3, 3, 3), "Yes")

    def test_different_numbers(self):
        """Test if function returns 'No' when a, b, and c are different."""
        self.assertEqual(Check_Solution(1, 2, 3), "No")

    def test_a_equal_c_and_b_different(self):
        """Test if function returns 'Yes' when a and c are the same but b is different."""
        self.assertEqual(Check_Solution(3, 4, 3), "Yes")

    def test_a_different_c_and_b_different(self):
        """Test if function returns 'No' when a, c, and b are different."""
        self.assertEqual(Check_Solution(1, 4, 3), "No")

    def test_a_equal_b_and_c_different(self):
        """Test if function returns 'Yes' when a and b are the same but c is different."""
        self.assertEqual(Check_Solution(3, 3, 4), "Yes")

    def test_negative_numbers(self):
        """Test if function works correctly with negative numbers."""
        self.assertEqual(Check_Solution(-1, -2, -3), "No")

    def test_zero_numbers(self):
        """Test if function works correctly with zero numbers."""
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")
