import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_password_length(self):
        self.assertTrue(pass_validity("a1b2C3$4"))
        self.assertTrue(pass_validity("1234567890"))
        self.assertTrue(pass_validity("abcdefghij"))
        self.assertTrue(pass_validity("ABCDEFGHIJ"))
        self.assertTrue(pass_validity("AbCdEfGhIj"))
        self.assertTrue(pass_validity("1234567890ABC"))
        self.assertTrue(pass_validity("abcdefghij12"))

    def test_invalid_password_length(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("aaa"))
        self.assertFalse(pass_validity("12345"))
        self.assertFalse(pass_validity("123456789"))
        self.assertFalse(pass_validity("abcdefghijkl"))
        self.assertFalse(pass_validity("ABCDEFGHIJKL"))
        self.assertFalse(pass_validity("AbCdEfGhIjKl"))
        self.assertFalse(pass_validity("123456789012"))

    def test_missing_char_types(self):
        self.assertFalse(pass_validity("abcdefg"))
        self.assertFalse(pass_validity("12345678"))
        self.assertFalse(pass_validity("ABCDEFGH"))
        self.assertFalse(pass_validity("$#@1234"))
        self.assertFalse(pass_validity("abc#def"))
        self.assertFalse(pass_validity("1234ABC"))
        self.assertFalse(pass_validity("abc@def"))

    def test_extra_char_types(self):
        self.assertFalse(pass_validity("abc123$#@"))
        self.assertFalse(pass_validity("ABC123$#@"))
        self.assertFalse(pass_validity("abc123$"))
        self.assertFalse(pass_validity("ABC123$"))
        self.assertFalse(pass_validity("abc123#"))
        self.assertFalse(pass_validity("ABC123#"))
        self.assertFalse(pass_validity("abc123@"))
        self.assertFalse(pass_validity("ABC123@"))

    def test_whitespace(self):
        self.assertFalse(pass_validity(" abc123 "))
        self.assertFalse(pass_validity("123 abc"))
        self.assertFalse(pass_validity("123 456"))
