import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")
        self.assertEqual(check_email("john.doe@example.org"), "Valid Email")
        self.assertEqual(check_email("jane_doe@example.co.uk"), "Valid Email")
        self.assertEqual(check_email("john.doe+123@example.com"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")
        self.assertEqual(check_email("test@example.c"), "Invalid Email")
        self.assertEqual(check_email("test@example.l"), "Invalid Email" )
        self.assertEqual(check_email("test@.example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co"), "Invalid Email")
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
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co.co.co.co.co.co.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.co.uk.co.co.co.co.co