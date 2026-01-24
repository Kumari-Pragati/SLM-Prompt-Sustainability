import unittest
from mbpp_822_code import pass_validity

class TestPasswordValidity(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(pass_validity('ValidPass123$'))

    def test_short_password(self):
        self.assertFalse(pass_validity('Short'))

    def test_long_password(self):
        self.assertFalse(pass_validity('ThisIsALongPasswordThatShouldNotBeValidBecauseItIsTooLong'))

    def test_missing_lowercase(self):
        self.assertFalse(pass_validity('VALIDPASS123$'))

    def test_missing_uppercase(self):
        self.assertFalse(pass_validity('validpass123$'))

    def test_missing_digit(self):
        self.assertFalse(pass_validity('validPass$'))

    def test_missing_special_char(self):
        self.assertFalse(pass_validity('validPass123'))

    def test_password_with_whitespace(self):
        self.assertFalse(pass_validity('valid Pass123$'))
