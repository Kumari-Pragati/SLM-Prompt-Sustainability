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
        self.assertEqual(check_email("test@example.com."), "Invalid Email")
        self.assertEqual(check_email("test@example.co"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.uk"), "Invalid Email")
        self.assertEqual(check_email("test@example.com@example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.123"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.aaa"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.aaa.aaa"), "Invalid Email")
        self.assertEqual(check_email("test@-example.com"), "Invalid Email")
        self.assertEqual(check_email("test@example.com_"), "Invalid Email")
        self.assertEqual(check_email("test@example.com.123@example.com"), "Invalid Email")
