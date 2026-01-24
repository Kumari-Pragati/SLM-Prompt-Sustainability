import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_remove_single_extra_char(self):
        self.assertEqual(remove_extra_char("Hello_World"), "HelloWorld")

    def test_remove_multiple_extra_chars(self):
        self.assertEqual(remove_extra_char("123__456"), "123456")

    def test_remove_extra_chars_with_numbers(self):
        self.assertEqual(remove_extra_char("123_456_789"), "123456789")

    def test_remove_extra_chars_with_special_characters(self):
        self.assertEqual(remove_extra_char("Hello!@#$%^&*()_+-="), "Hello")

    def test_remove_extra_chars_with_spaces(self):
        self.assertEqual(remove_extra_char(" Hello World "), "HelloWorld")

    def test_remove_extra_chars_with_only_spaces(self):
        self.assertEqual(remove_extra_char("   "), "")

    def test_remove_extra_chars_with_empty_string(self):
        self.assertEqual(remove_extra_char(""), "")
