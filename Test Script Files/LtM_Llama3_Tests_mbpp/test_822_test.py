import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_pass(self):
        self.assertTrue(pass_validity("Hello123$"))

    def test_invalid_pass(self):
        self.assertFalse(pass_validity("Hello"))
        self.assertFalse(pass_validity("123456"))
        self.assertFalse(pass_validity("HELLO"))
        self.assertFalse(pass_validity("hello123$"))
        self.assertFalse(pass_validity("hello123"))
        self.assertFalse(pass_validity("hello123$@"))
        self.assertFalse(pass_validity("hello123@"))
        self.assertFalse(pass_validity("hello123$#"))
        self.assertFalse(pass_validity("hello123#"))
        self.assertFalse(pass_validity("hello123$@#"))
        self.assertFalse(pass_validity("hello123@#"))
        self.assertFalse(pass_validity("hello123$#"))
        self.assertFalse(pass_validity("hello123#"))
        self.assertFalse(pass_validity("hello123$@#"))

    def test_pass_length(self):
        self.assertFalse(pass_validity("Hello"))
        self.assertFalse(pass_validity("123456"))
        self.assertTrue(pass_validity("Hello123"))
        self.assertTrue(pass_validity("Hello1234"))
        self.assertTrue(pass_validity("Hello12345"))
        self.assertFalse(pass_validity("Hello1234567"))

    def test_pass_characters(self):
        self.assertFalse(pass_validity("Hello"))
        self.assertFalse(pass_validity("123456"))
        self.assertTrue(pass_validity("Hello123$"))
        self.assertTrue(pass_validity("Hello123@"))
        self.assertTrue(pass_validity("Hello123#"))
        self.assertTrue(pass_validity("Hello123$@#"))

    def test_pass_spaces(self):
        self.assertFalse(pass_validity("Hello 123$"))
