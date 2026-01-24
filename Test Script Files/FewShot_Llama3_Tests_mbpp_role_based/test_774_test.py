import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("invalid_email"), "Invalid Email")

    def test_email_with_spaces(self):
        self.assertEqual(check_email("test@example.com with spaces"), "Invalid Email")

    def test_email_without_at_symbol(self):
        self.assertEqual(check_email("testexample.com"), "Invalid Email")

    def test_email_without_domain(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")

    def test_email_with_invalid_characters(self):
        self.assertEqual(check_email("test!example.com"), "Invalid Email")

    def test_empty_string(self):
        self.assertEqual(check_email(""), "Invalid Email")
