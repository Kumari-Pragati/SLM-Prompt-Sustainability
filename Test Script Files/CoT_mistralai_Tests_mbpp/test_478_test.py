import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_single_uppercase_letter(self):
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertEqual(remove_lowercase(char), char)

    def test_single_lowercase_letter(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(remove_lowercase(char), '')

    def test_mixed_case_string(self):
        test_str = 'HelloWorld123_456'
        expected_result = 'HW123_456'
        self.assertEqual(remove_lowercase(test_str), expected_result)

    def test_string_with_only_lowercase_letters(self):
        test_str = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(remove_lowercase(test_str), '')

    def test_string_with_only_uppercase_letters(self):
        test_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertEqual(remove_lowercase(test_str), test_str)

    def test_string_with_numbers_and_special_characters(self):
        test_str = '123!@#$%^&*()_+-=[]{}|;:'\''<,>.?/'
        self.assertEqual(remove_lowercase(test_str), test_str)

    def test_string_with_numbers_and_special_characters_and_mixed_case(self):
        test_str = '123!@#$%^&*()_+-=[]{}|;:'\''<,>.?/HelloWorld'
        expected_result = '123!@#$%^&*()_+-=[]{}|;:'\''<,>.?/'
        self.assertEqual(remove_lowercase(test_str), expected_result)
