import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')

    def test_invalid_email(self):
        self.assertEqual(check_email('test@example'), 'Invalid Email')

    def test_empty_email(self):
        self.assertEqual(check_email(''), 'Invalid Email')

    def test_email_with_special_characters(self):
        self.assertEqual(check_email('test@exa#mple.com'), 'Invalid Email')

    def test_email_with_numbers_and_special_characters(self):
        self.assertEqual(check_email('test123@exa#mple.com'), 'Invalid Email')

    def test_email_with_multiple_at_symbols(self):
        self.assertEqual(check_email('test@test@example.com'), 'Invalid Email')

    def test_email_with_multiple_dot_symbols(self):
        self.assertEqual(check_email('test@example..com'), 'Invalid Email')

    def test_email_with_underscores(self):
        self.assertEqual(check_email('test_test@example.com'), 'Valid Email')

    def test_email_with_numbers_and_underscores(self):
        self.assertEqual(check_email('test123_test@example.com'), 'Valid Email')

    def test_email_with_special_characters_after_at(self):
        self.assertEqual(check_email('test@exa#mple.com'), 'Invalid Email')

    def test_email_with_special_characters_after_dot(self):
        self.assertEqual(check_email('test@example.com#'), 'Invalid Email')
