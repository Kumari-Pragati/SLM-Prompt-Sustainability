import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_empty_string(self):
        """Test for empty string"""
        self.assertEqual(check_Equality(""), "Equal")

    def test_single_character_string(self):
        """Test for single character string"""
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(check_Equality(char), "Equal")

    def test_palindrome(self):
        """Test for palindrome strings"""
        palindromes = ["level", "madam", "racecar", "radar"]
        for palindrome in palindromes:
            self.assertEqual(check_Equality(palindrome), "Equal")

    def test_non_palindrome(self):
        """Test for non-palindrome strings"""
        non_palindromes = ["python", "javascript", "hello", "world"]
        for non_palindrome in non_palindromes:
            self.assertEqual(check_Equality(non_palindrome), "Not Equal")

    def test_mixed_case_string(self):
        """Test for mixed case strings"""
        mixed_case_strings = ["Python", "JavaScript", "Hello", "World"]
        for mixed_case_string in mixed_case_strings:
            self.assertEqual(check_Equality(mixed_case_string), "Not Equal")

    def test_whitespace_string(self):
        """Test for strings with whitespace"""
        whitespace_strings = ["  ", " a b ", "foo bar"]
        for whitespace_string in whitespace_strings:
            self.assertEqual(check_Equality(whitespace_string), "Not Equal")
