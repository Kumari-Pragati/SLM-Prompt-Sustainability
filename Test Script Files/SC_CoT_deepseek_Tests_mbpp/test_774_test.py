import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_typical_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')

    def test_email_with_dot_in_username(self):
        self.assertEqual(check_email('test.name@example.com'), 'Valid Email')

    def test_email_with_underscore_in_username(self):
        self.assertEqual(check_email('test_name@example.com'), 'Valid Email')

    def test_email_with_dot_and_underscore_in_username(self):
        self.assertEqual(check_email('test.name_123@example.com'), 'Valid Email')

    def test_email_with_single_character_username(self):
        self.assertEqual(check_email('t@example.com'), 'Valid Email')

    def test_email_with_single_character_domain(self):
        self.assertEqual(check_email('test@e.com'), 'Valid Email')

    def test_email_with_numbers_in_domain(self):
        self.assertEqual(check_email('test@example123.com'), 'Valid Email')

    def test_email_with_special_characters_in_domain(self):
        self.assertEqual(check_email('test@example_123.com'), 'Valid Email')

    def test_email_with_multiple_dots_in_domain(self):
        self.assertEqual(check_email('test@example.co.uk'), 'Valid Email')

    def test_email_with_single_character_tld(self):
        self.assertEqual(check_email('test@example.c'), 'Valid Email')

    def test_email_with_two_characters_tld(self):
        self.assertEqual(check_email('test@example.co'), 'Valid Email')

    def test_email_with_three_characters_tld(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')

    def test_email_with_no_username(self):
        self.assertEqual(check_email('@example.com'), 'Invalid Email')

    def test_email_with_no_domain(self):
        self.assertEqual(check_email('test@'), 'Invalid Email')

    def test_email_with_no_at_symbol(self):
        self.assertEqual(check_email('testexample.com'), 'Invalid Email')

    def test_email_with_multiple_at_symbols(self):
        self.assertEqual(check_email('test@test@example.com'), 'Invalid Email')

    def test_email_with_special_characters_in_username(self):
        self.assertEqual(check_email('te$t@example.com'), 'Invalid Email')

    def test_email_with_numbers_in_domain(self):
        self.assertEqual(check_email('test@123example.com'), 'Invalid Email')

    def test_email_with_special_characters_in_domain(self):
        self.assertEqual(check_email('test@exa#mple.com'), 'Invalid Email')

    def test_email_with_multiple_dots_in_username(self):
        self.assertEqual(check_email('te.st@example.com'), 'Invalid Email')
