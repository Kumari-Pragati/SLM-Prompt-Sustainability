import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_empty_string(self):
        """Test if the function returns 0 for an empty string"""
        self.assertEqual(upper_ctr(''), 0)

    def test_all_uppercase(self):
        """Test if the function correctly counts all uppercase letters"""
        self.assertEqual(upper_ctr('HELLO'), 5)

    def test_mixed_case(self):
        """Test if the function correctly counts uppercase letters in a mixed case string"""
        self.assertEqual(upper_ctr('HelloWorld'), 2)

    def test_single_uppercase(self):
        """Test if the function correctly counts a single uppercase letter"""
        self.assertEqual(upper_ctr('A'), 1)

    def test_boundary_cases(self):
        """Test if the function correctly handles boundary cases"""
        self.assertEqual(upper_ctr('Z'), 1)
        self.assertEqual(upper_ctr('A' * 100), 100)

    def test_non_alphabet_characters(self):
        """Test if the function correctly ignores non-alphabet characters"""
        self.assertEqual(upper_ctr('Hello123'), 2)
