import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(pass_validity("a1b2C3$d4E5"))
        self.assertTrue(pass_validity("A1B2c3$D4E5"))
        self.assertTrue(pass_validity("a1b2c3$d4e5"))
        self.assertTrue(pass_validity("A1B2C3$D4E5_"))
        self.assertTrue(pass_validity("a1b2c3$d4e5_"))
        self.assertTrue(pass_validity("A1B2c3$D4E5_1"))
        self.assertTrue(pass_validity("a1b2c3$d4e5_1"))

    def test_invalid_password_length(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("abcdefg"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(pass_validity("1234567890"))
        self.assertFalse(pass_validity("12345678901234567890"))

    def test_invalid_characters(self):
        self.assertFalse(pass_validity("abcd"))
        self.assertFalse(pass_validity("1234"))
        self.assertFalse(pass_validity("ABCD"))
        self.assertFalse(pass_validity("!@#"))
        self.assertFalse(pass_validity("$%^&*"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz01234567890"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz$%^&*"))

    def test_invalid_special_characters(self):
        self.assertFalse(pass_validity("$"))
        self.assertFalse(pass_validity("@"))
        self.assertFalse(pass_validity("#"))
        self.assertFalse(pass_validity("@#"))
        self.assertFalse(pass_validity("$@"))
        self.assertFalse(pass_validity("!@#$"))
        self.assertFalse(pass_validity("$%"))
        self.assertFalse(pass_validity("@#$"))
        self.assertFalse(pass_validity("!@#$%"))

    def test_invalid_whitespace(self):
        self.assertFalse(pass_validity(" a1b2C3$d4E5 "))
        self.assertFalse(pass_validity(" A1B2c3$d4E5 "))
        self.assertFalse(pass_validity(" a1b2c3$d4e5 "))
        self.assertFalse(pass_validity(" A1B2C3$D4E5_ "))
        self.assertFalse(pass_validity(" a1b2c3$d4e5_ "))
        self.assertFalse(pass_validity(" A1B2c3$D4E5_1 "))
        self.assertFalse(pass_validity(" a1b2c3$d4e5_1 "))
