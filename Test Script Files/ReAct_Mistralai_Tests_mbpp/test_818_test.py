import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_empty_string(self):
        """Test lower_ctr on an empty string"""
        self.assertEqual(lower_ctr(''), 0)

    def test_single_uppercase_letter(self):
        """Test lower_ctr on a single uppercase letter"""
        self.assertEqual(lower_ctr('A'), 0)

    def test_single_lowercase_letter(self):
        """Test lower_ctr on a single lowercase letter"""
        self.assertEqual(lower_ctr('a'), 1)

    def test_mixed_case_string(self):
        """Test lower_ctr on a mixed case string"""
        self.assertEqual(lower_ctr('Hello, World!'), 10)

    def test_long_string(self):
        """Test lower_ctr on a long string"""
        long_string = 'x' * 100
        self.assertEqual(lower_ctr(long_string), len(long_string))

    def test_string_with_only_digits(self):
        """Test lower_ctr on a string with only digits"""
        self.assertEqual(lower_ctr('123456'), 0)

    def test_string_with_special_characters(self):
        """Test lower_ctr on a string with special characters"""
        self.assertEqual(lower_ctr('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)
