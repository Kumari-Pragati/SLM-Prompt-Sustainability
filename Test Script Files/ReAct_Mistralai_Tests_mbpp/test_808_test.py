import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_empty_list(self):
        """Check if function returns False for an empty list."""
        self.assertFalse(check_K([], 1))

    def test_single_element_list(self):
        """Check if function returns True for a list containing the correct element."""
        self.assertTrue(check_K([1], 1))

    def test_multiple_elements_list(self):
        """Check if function returns True for a list containing the correct element."""
        self.assertTrue(check_K([1, 2, 3, 4, 5], 1))

    def test_non_matching_element(self):
        """Check if function returns False for a list containing a non-matching element."""
        self.assertFalse(check_K([1, 2, 3, 4, 5], 6))

    def test_negative_number(self):
        """Check if function handles negative numbers correctly."""
        self.assertTrue(check_K([-1, 2, 3, 4, 5], -1))

    def test_zero_number(self):
        """Check if function handles zero correctly."""
        self.assertTrue(check_K([0, 2, 3, 4, 5], 0))

    def test_float_number(self):
        """Check if function handles float numbers correctly."""
        self.assertTrue(check_K([1.1, 2, 3, 4, 5], 1.1))

    def test_list_with_duplicates(self):
        """Check if function returns True for a list containing the correct element multiple times."""
        self.assertTrue(check_K([1, 1, 2, 3, 4, 5], 1))
