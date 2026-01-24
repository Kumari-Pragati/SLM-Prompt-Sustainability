import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_empty_list(self):
        """Test if the function returns -1 when given an empty list."""
        self.assertEqual(first_even([]), -1)

    def test_single_odd_number(self):
        """Test if the function returns -1 when given a list containing only an odd number."""
        self.assertEqual(first_even([1]), -1)

    def test_single_even_number(self):
        """Test if the function returns the single even number when given a list containing only an even number."""
        self.assertEqual(first_even([2]), 2)

    def test_multiple_even_numbers(self):
        """Test if the function returns the first even number when given a list containing multiple even numbers."""
        self.assertEqual(first_even([2, 4, 6]), 2)

    def test_multiple_odd_numbers(self):
        """Test if the function returns -1 when given a list containing multiple odd numbers."""
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_mixed_numbers(self):
        """Test if the function returns the first even number when given a list containing a mix of odd and even numbers."""
        self.assertEqual(first_even([1, 2, 3, 4, 5, 6]), 2)

    def test_negative_numbers(self):
        """Test if the function works correctly with negative numbers."""
        self.assertEqual(first_even([2, -4, 6, -2]), 2)

    def test_large_numbers(self):
        """Test if the function works correctly with large numbers."""
        self.assertEqual(first_even([10000, 10002, 10004]), 10000)
