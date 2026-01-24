import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(pass_validity("A1b2c3D4E5f6"))
        self.assertTrue(pass_validity("a1B2c3d4E5F6"))
        self.assertTrue(pass_validity("A1b2c3d4e5F6"))
        self.assertTrue(pass_validity("A1b2c3d4e5F67"))
        self.assertTrue(pass_validity("A1b2c3d4e5F6789"))
        self.assertTrue(pass_validity("A1b2c3d4e5F67890"))

    def test_min_length(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("ab"))
        self.assertFalse(pass_validity("abc"))
        self.assertFalse(pass_validity("abcd"))
        self.assertFalse(pass_validity("abcd1"))
        self.assertFalse(pass_validity("abcd12"))

    def test_max_length(self):
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(pass_validity("1234567890"))
        self.assertFalse(pass_validity("12345678901"))
        self.assertFalse(pass_validity("123456789012"))
        self.assertFalse(pass_validity("1234567890123"))

    def test_no_lowercase(self):
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ1"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ12"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ123"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234"))
        self.assertFalse(pass_validity("ABCDEFGHIJKLMNOPQRSTUVWXYZ12345"))

    def test_no_uppercase(self):
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz1"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz12"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz123"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz1234"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz12345"))

    def test_no_digits(self):
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz "))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyzAB"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyzABC"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyzABCDE"))
        self.assertFalse(pass_validity("abcdefghijklmnopq