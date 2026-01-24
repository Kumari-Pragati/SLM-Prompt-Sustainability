import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")
        self.assertEqual(check_email("test.example@com"), "Valid Email")
        self.assertEqual(check_email("test_123@example.co.uk"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.uk"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.123"), "Invalid Email")
        self.assertEqual(check_email("test@example.com."), "Invalid Email")
        self.assertEqual(check_email("test@.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com@example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.example.example"), "Invalid Email")
