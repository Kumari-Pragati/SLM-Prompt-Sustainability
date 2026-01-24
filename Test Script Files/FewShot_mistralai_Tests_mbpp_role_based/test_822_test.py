import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_password_length(self):
        self.assertTrue(pass_validity("a1B2c3D4$5"))
        self.assertTrue(pass_validity("a1b2C3d4$56"))
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("a1b2c3d4"))
        self.assertFalse(pass_validity("a1b2c3d4$"))
        self.assertFalse(pass_validity("a1b2c3d4$#"))
        self.assertFalse(pass_validity("a1b2c3d4$#@"))
        self.assertFalse(pass_validity("a1b2c3d4$#@!"))

    def test_invalid_password_length(self):
        self.assertFalse(pass_validity(""))
        self.assertFalse(pass_validity("aaa"))
        self.assertFalse(pass_validity("1234567890"))
        self.assertFalse(pass_validity("123456789012"))

    def test_invalid_characters(self):
        self.assertFalse(pass_validity("abcdefg"))
        self.assertFalse(pass_validity("123456"))
        self.assertFalse(pass_validity("ABCDEFG"))
        self.assertFalse(pass_validity("$#@"))
