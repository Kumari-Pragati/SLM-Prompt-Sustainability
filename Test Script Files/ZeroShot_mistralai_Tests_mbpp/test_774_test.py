import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")
        self.assertEqual(check_email("test_123@example.co.uk"), "Valid Email")
        self.assertEqual(check_email("test.123@example.com"), "Valid Email")
        self.assertEqual(check_email("test123@example.com"), "Valid Email")
        self.assertEqual(check_email("test123.123@example.com"), "Valid Email")
        self.assertEqual(check_email("test123.123@example.org"), "Valid Email")
        self.assertEqual(check_email("test123.123@example.net"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")
        self.assertEqual(check_email("test@example."), "Invalid Email")
        self.assertEqual(check_email("test@.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.co.uk."), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk."), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk@example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com@example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example.com.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example.com.example.com.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example.com.example.com.example.com.example.com"), "Invalid Email")
