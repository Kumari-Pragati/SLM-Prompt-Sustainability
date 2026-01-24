import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_empty_list(self):
        """Test if an empty list returns an empty list."""
        self.assertListEqual(larg_nnum([], 3), [])

    def test_single_element(self):
        """Test if a list with a single element returns that element."""
        self.assertListEqual(larg_nnum([1], 1), [1])

    def test_multiple_elements(self):
        """Test if a list with multiple elements returns the n largest elements."""
        self.assertListEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_n_larger_than_length(self):
        """Test if n is larger than the list length, returns the entire list."""
        self.assertListEqual(larg_nnum([1, 2, 3], 4), [1, 2, 3])

    def test_negative_n(self):
        """Test if n is negative, raises a ValueError."""
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3], -1)

    def test_non_list_input(self):
        """Test if input is not a list, raises a TypeError."""
        with self.assertRaises(TypeError):
            larg_nnum('str', 3)
