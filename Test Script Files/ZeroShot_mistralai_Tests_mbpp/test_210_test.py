import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_allowed_special_char(''))

    def test_only_allowed_characters(self):
        self.assertTrue(is_allowed_special_char('abc123.@'))

    def test_only_disallowed_characters(self):
        self.assertFalse(is_allowed_special_char('!@#$%^&*()_+-=[]{};:'\
                                                 '|\\/~`'))

    def test_mixed_allowed_and_disallowed_characters(self):
        self.assertTrue(is_allowed_special_char('abc123.@!@#$%^&*()_+-=[]{};:'\
                                                 '|\\/~`'))
