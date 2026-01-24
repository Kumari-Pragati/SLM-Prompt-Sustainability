import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(pass_validity("A1b2C3d4E5$6"))
        self.assertTrue(pass_validity("a1B2c3D4e5$6"))
        self.assertTrue(pass_validity("A1b2c3d4E5$67"))
        self.assertTrue(pass_validity("a1b2c3d4e5$678"))

    def test_invalid_password_length(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("aaaaaaa"))
        self.assertFalse(pass_validity("aaaaaaaaaaaaaaaa"))

    def test_missing_char_types(self):
        self.assertFalse(pass_validity("123456"))
        self.assertFalse(pass_validity("ABCDEFG"))
        self.assertFalse(pass_validity("!@#$%"))
        self.assertFalse(pass_validity("   "))

    def test_invalid_characters( self ):
        self.assertFalse(pass_validity("A1b2c3d4E5$6!"))
        self.assertFalse(pass_validity("A1b2c3d4E5$6@"))
        self.assertFalse(pass_validity("A1b2c3d4E5$6#"))
        self.assertFalse(pass_validity("A1b2c3d4E5$6$"))
