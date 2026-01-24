import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test"), "Invalid Email")

    def test_valid_email_with_domain(self):
        self.assertEqual(check_email("test@example.co.uk"), "Valid Email")

    def test_valid_email_with_subdomain(self):
        self.assertEqual(check_email("test@subdomain.example.com"), "Valid Email")

    def test_invalid_email_without_at_symbol(self):
        self.assertEqual(check_email("testexample.com"), "Invalid Email")

    def test_invalid_email_without_domain(self):
        self.assertEqual(check_email("test@"), "Invalid Email")

    def test_invalid_email_without_local_part(self):
        self.assertEqual(check_email("@example.com"), "Invalid Email")

    def test_invalid_email_without_top_level_domain(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")

    def test_invalid_email_with_non_alphanumeric_characters(self):
        self.assertEqual(check_email("test!example.com"), "Invalid Email")

    def test_invalid_email_with_non_ascii_characters(self):
        self.assertEqual(check_email("testü@example.com"), "Invalid Email")
