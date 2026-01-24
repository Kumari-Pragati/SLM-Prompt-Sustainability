import unittest
from mbpp_436_code import neg_nos

class TestNegativeNumbers(unittest.TestCase):

    def test_positive_list(self):
        """Test that function returns None for a list of positive numbers."""
        result = neg_nos([3, 5, 7])
        self.assertIsNone(result)

    def test_zero(self):
        """Test that function returns None for a list containing zero."""
        result = neg_nos([0])
        self.assertIsNone(result)

    def test_negative_single(self):
        """Test that function correctly returns a negative number."""
        result = neg_nos([-5])
        self.assertEqual(result, -5)

    def test_negative_multiple(self):
        """Test that function correctly returns the first negative number in a list."""
        result = neg_nos([-5, 3, -2, 7])
        self.assertEqual(result, -5)

    def test_empty_list(self):
        """Test that function returns None for an empty list."""
        result = neg_nos([])
        self.assertIsNone(result)

    def test_negative_list_only(self):
        """Test that function correctly returns the first negative number in a list of negatives."""
        result = neg_nos([-5, -3, -2])
        self.assertEqual(result, -5)

    def test_float_positive(self):
        """Test that function correctly handles positive floating point numbers."""
        result = neg_nos([3.14, 2.718])
        self.assertIsNone(result)

    def test_float_negative(self):
        """Test that function correctly handles negative floating point numbers."""
        result = neg_nos([-3.14, -2.718])
        self.assertEqual(result, -3.14)
