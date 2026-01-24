import unittest
from mbpp_485_code import largest_palindrome

class TestLargestPalindrome(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_palindrome([], 1), -1)

    def test_single_element(self):
        self.assertEqual(largest_palindrome([123], 1), -1)
        self.assertEqual(largest_palindrome([121], 1), 121)

    def test_multiple_elements(self):
        self.assertEqual(largest_palindrome([123, 121, 1234, 1221], 1), 121)
        self.assertEqual(largest_palindrome([123, 121, 1234, 1221], 2), -1)

    def test_large_numbers(self):
        self.assertEqual(largest_palindrome([123456789, 122122121, 1230321, 1234567890], 1), 122122121)
        self.assertEqual(largest_palindrome([123456789, 122122121, 1230321, 1234567890], 2), 1230321)

    def test_negative_numbers(self):
        self.assertEqual(largest_palindrome([-123, -121, -1234, -1221], 1), -121)
        self.assertEqual(largest_palindrome([-123, -121, -1234, -1221], 2), -1)

    def test_sort_function(self):
        # Test if the sort function works correctly
        data = [123, 121, 1234, 1221]
        largest_palindrome(data, 1)
        self.assertEqual(data, [-1221, 121, 123, 1234])
