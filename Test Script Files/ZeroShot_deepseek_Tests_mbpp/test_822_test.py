import unittest
from mbpp_822_code import pass_validity

class TestPasswordValidity(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(pass_validity("Abc123$"))
        self.assertTrue(pass_validity("abc123$"))
        self.assertTrue(pass_validity("Abc123$"))
        self.assertTrue(pass_validity("Abcdef123$"))

    def test_invalid_password(self):
        self.assertFalse(pass_validity("abc"))
        self.assertFalse(pass_validity("Abcdefg1234"))
        self.assertFalse(pass_validity("Abcdef123"))
        self.assertFalse(pass_validity("Abcdef123$ "))
        self.assertFalse(pass_validity("Abcdef123#"))
        self.assertFalse(pass_validity("abcdef123$"))
        self.assertFalse(pass_validity("ABCDEF123$"))
