import unittest
from mbpp_554_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns an empty list"""
        result = Split([])
        self.assertListEqual(result, [])

    def test_single_even_number(self):
        """Test that a single even number returns an empty list"""
        result = Split([2])
        self.assertListEqual(result, [])

    def test_single_odd_number(self):
        """Test that a single odd number returns the odd number"""
        result = Split([5])
        self.assertListEqual(result, [5])

    def test_multiple_odd_numbers(self):
        """Test that multiple odd numbers are collected into a list"""
        result = Split([1, 3, 5, 7])
        self.assertListEqual(result, [1, 3, 5, 7])

    def test_mixed_numbers(self):
        """Test that odd numbers are collected from a list of mixed numbers"""
        result = Split([2, 4, 1, 3, 6, 5])
        self.assertListEqual(result, [1, 3, 5])

    def test_large_list(self):
        """Test that the function can handle large lists"""
        result = Split([i for i in range(1000, 1000 + 100, 2)])
        self.assertListEqual(result, list(range(1000, 1000 + 100, 2)))

    def test_negative_numbers(self):
        """Test that the function can handle negative odd numbers"""
        result = Split([-1, -3, -5])
        self.assertListEqual(result, [-1, -3, -5])
