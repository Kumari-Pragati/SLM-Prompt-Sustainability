import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_empty_list(self):
        """Test if function returns 0 for an empty list"""
        self.assertEqual(count_odd([]), 0)

    def test_single_even_number(self):
        """Test if function returns 0 for a list containing only even numbers"""
        self.assertEqual(count_odd([2, 4, 6]), 0)

    def test_single_odd_number(self):
        """Test if function returns 1 for a list containing only one odd number"""
        self.assertEqual(count_odd([1]), 1)

    def test_multiple_odd_numbers(self):
        """Test if function correctly counts multiple odd numbers"""
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_mixed_numbers(self):
        """Test if function correctly counts odd numbers in a mixed list"""
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_large_list(self):
        """Test if function can handle large lists"""
        large_list = [i for i in range(10000)]
        self.assertEqual(count_odd(large_list), 4999)

    def test_negative_numbers(self):
        """Test if function correctly counts odd negative numbers"""
        self.assertEqual(count_odd([-1, -3, -5]), 3)

    def test_floats(self):
        """Test if function correctly counts odd floating point numbers"""
        self.assertEqual(count_odd([1.1, 2.2, 3.3]), 1)

    def test_list_with_non_numbers(self):
        """Test if function correctly ignores non-numbers in the list"""
        self.assertEqual(count_odd(['a', 1, 'b', 3, 'c']), 2)
