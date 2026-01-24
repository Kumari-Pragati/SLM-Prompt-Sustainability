import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumber(unittest.TestCase):

    def test_valid_months(self):
        """Test that the function correctly identifies valid months."""
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_invalid_months(self):
        """Test that the function correctly identifies invalid months."""
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(7))
        self.assertFalse(check_monthnumber_number(8))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(-1))
        self.assertFalse(check_monthnumber_number(13))

    def test_zero_and_non_integer_inputs(self):
        """Test that the function correctly handles non-integer and zero inputs."""
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(3.14))
        self.assertFalse(check_monthnumber_number('str'))
