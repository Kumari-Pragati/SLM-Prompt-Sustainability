import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_pass(self):
        self.assertTrue(pass_validity("Password123"))

    def test_invalid_length_pass(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("123456789012345678901234567890"))

    def test_invalid_char_pass(self):
        self.assertFalse(pass_validity("password123"))
        self.assertFalse(pass_validity("Password123456"))

    def test_valid_pass_with_special_char(self):
        self.assertTrue(pass_validity("Password123$"))

    def test_invalid_pass_with_space(self):
        self.assertFalse(pass_validity("Password 123"))

    def test_invalid_pass_with_non_alpha_num_special_char(self):
        self.assertFalse(pass_validity("Password!@#"))

    def test_invalid_pass_with_non_alpha_num_special_char_and_space(self):
        self.assertFalse(pass_validity("Password!@#"))
