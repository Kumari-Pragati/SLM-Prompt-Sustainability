import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns 0"""
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        """Test that a list with one element returns the correct sum"""
        self.assertEqual(count([1]), 1)

    def test_positive_numbers_list(self):
        """Test that a list of positive numbers returns the correct sum"""
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers_list(self):
        """Test that a list of negative numbers returns the correct sum"""
        self.assertEqual(count([-1, -2, -3, -4, -5]), 15)

    def test_mixed_numbers_list(self):
        """Test that a list of mixed numbers returns the correct sum"""
        self.assertEqual(count([1, -2, 3, -4, 5]), 6)

    def test_large_list(self):
        """Test that a large list returns the correct sum"""
        large_list = [i for i in range(1000)]
        self.assertEqual(count(large_list), sum(range(1, 1001)))

    def test_list_with_zero(self):
        """Test that a list with zero returns the correct sum"""
        self.assertEqual(count([0]), 0)

    def test_list_with_floats(self):
        """Test that a list with floats returns the correct sum"""
        self.assertEqual(count([1.1, 2.2, 3.3]), 6.6)

    def test_list_with_strings(self):
        """Test that a list with strings raises a ValueError"""
        with self.assertRaises(ValueError):
            count(["a", "b", "c"])
