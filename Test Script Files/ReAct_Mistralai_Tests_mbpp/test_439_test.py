import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_empty_list(self):
        """Test if an empty list returns 0"""
        self.assertEqual(multiple_to_single([]), 0)

    def test_single_element(self):
        """Test if a single element list returns the same number"""
        self.assertEqual(multiple_to_single([5]), 5)

    def test_positive_numbers(self):
        """Test if multiple positive numbers are correctly combined"""
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_negative_numbers(self):
        """Test if multiple negative numbers are correctly combined"""
        self.assertEqual(multiple_to_single([-1, -2, -3, -4, -5]), 12345)

    def test_mixed_numbers(self):
        """Test if a mix of positive and negative numbers are correctly combined"""
        self.assertEqual(multiple_to_single([1, -2, 3, -4, 5]), 13-4)

    def test_zero(self):
        """Test if zero is correctly handled"""
        self.assertEqual(multiple_to_single([0]), 0)
        self.assertEqual(multiple_to_single([0, 1, 0]), 1)
        self.assertEqual(multiple_to_single([0, 0, 0]), 0)

    def test_non_integer_elements(self):
        """Test if non-integer elements raise a ValueError"""
        self.assertRaises(ValueError, multiple_to_single, [1, 'a', 2])
        self.assertRaises(ValueError, multiple_to_single, ['a', 1, 'b', 2])
