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

    def test_valid_email_with_numbers(self):
        self.assertEqual(check_email("test123@example.com"), "Valid Email")

    def test_valid_email_with_special_chars(self):
        self.assertEqual(check_email("test!@example.com"), "Valid Email")

    def test_valid_email_with_long_domain(self):
        self.assertEqual(check_email("test@example.com.mx"), "Valid Email")

    def test_valid_email_with_long_subdomain(self):
        self.assertEqual(check_email("test@subdomain.subdomain.example.com"), "Valid Email")

    def test_invalid_email_with_no_at_symbol(self):
        self.assertEqual(check_email("testexample.com"), "Invalid Email")

    def test_invalid_email_with_no_domain(self):
        self.assertEqual(check_email("test@"), "Invalid Email")

    def test_invalid_email_with_no_tld(self):
        self.assertEqual(check_email("test@example.com."), "Invalid Email")

    def test_invalid_email_with_no_local_part(self):
        self.assertEqual(check_email("@example.com"), "Invalid Email")

    def test_invalid_email_with_no_local_part_and_no_at_symbol(self):
        self.assertEqual(check_email("example.com"), "Invalid Email")

    def test_invalid_email_with_no_local_part_and_no_at_symbol_and_no_tld(self):
        self.assertEqual(check_email("example"), "Invalid Email")
