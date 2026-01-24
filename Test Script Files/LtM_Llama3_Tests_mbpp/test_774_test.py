import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test"), "Invalid Email")

    def test_empty_email(self):
        self.assertEqual(check_email(""), "Invalid Email")

    def test_invalid_characters(self):
        self.assertEqual(check_email("test@.com"), "Invalid Email")

    def test_missing_domain(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")

    def test_missing_extension(self):
        self.assertEqual(check_email("test@example.com."), "Invalid Email")

    def test_multiple_dots(self):
        self.assertEqual(check_email("test..@example.com"), "Invalid Email")

    def test_multiple_dashes(self):
        self.assertEqual(check_email("test-@example.com"), "Invalid Email")

    def test_valid_email_with_numbers(self):
        self.assertEqual(check_email("test123@example.com"), "Valid Email")

    def test_valid_email_with_special_characters(self):
        self.assertEqual(check_email("test!@example.com"), "Valid Email")
