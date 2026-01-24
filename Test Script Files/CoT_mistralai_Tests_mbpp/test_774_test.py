import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")
        self.assertEqual(check_email("test.example@com"), "Valid Email")
        self.assertEqual(check_email("test_123@example.co.uk"), "Valid Email")
        self.assertEqual(check_email("test.123@example.org"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")
        self.assertEqual(check_email("test@.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.a"), "Invalid Email" )
        self.assertEqual(check_email("test@example.aa"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.uk"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co