import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns 0"""
        self.assertEqual(count_integer([]), 0)

    def test_all_integers(self):
        """Test that a list of integers returns the correct count"""
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_mixed_types(self):
        """Test that a list with mixed types returns the correct count"""
        self.assertEqual(count_integer([1, 'a', 2, 'b', 3]), 3)

    def test_negative_numbers(self):
        """Test that negative numbers are correctly counted"""
        self.assertEqual(count_integer([-1, -2, -3]), 3)

    def test_zero(self):
        """Test that the integer 0 is correctly counted"""
        self.assertEqual(count_integer([0]), 1)

    def test_large_numbers(self):
        """Test that large numbers are correctly counted"""
        self.assertEqual(count_integer([1000000, 2000000, 3000000]), 3)

    def test_floats(self):
        """Test that floats are not counted"""
        self.assertEqual(count_integer([1.0, 2.0, 3.0]), 0)

    def test_complex_numbers(self):
        """Test that complex numbers are not counted"""
        self.assertEqual(count_integer([1j, 2j, 3j]), 0)
