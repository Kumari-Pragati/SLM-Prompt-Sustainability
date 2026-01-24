import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')

    def test_invalid_email(self):
        self.assertEqual(check_email('test@example'), 'Invalid Email')

    def test_missing_at_symbol(self):
        self.assertEqual(check_email('testexample.com'), 'Invalid Email')

    def test_missing_dot(self):
        self.assertEqual(check_email('test@examplecom'), 'Invalid Email')

    def test_empty_string(self):
        self.assertEqual(check_email(''), 'Invalid Email')

    def test_special_characters(self):
        self.assertEqual(check_email('test@exa#mple.com'), 'Invalid Email')
