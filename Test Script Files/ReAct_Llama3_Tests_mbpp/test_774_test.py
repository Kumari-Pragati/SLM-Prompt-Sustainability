import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email("test@example.com"), "Valid Email")

    def test_invalid_email(self):
        self.assertEqual(check_email("test"), "Invalid Email")

    def test_invalid_email2(self):
        self.assertEqual(check_email("test.example.com"), "Invalid Email")

    def test_valid_email2(self):
        self.assertEqual(check_email("test@example.co.uk"), "Valid Email")

    def test_invalid_email3(self):
        self.assertEqual(check_email("test@.com"), "Invalid Email")

    def test_invalid_email4(self):
        self.assertEqual(check_email("test@example"), "Invalid Email")

    def test_invalid_email5(self):
        self.assertEqual(check_email("test"), "Invalid Email")

    def test_invalid_email6(self):
        self.assertEqual(check_email("test.example"), "Invalid Email")

    def test_invalid_email7(self):
        self.assertEqual(check_email("test@.com."), "Invalid Email")

    def test_invalid_email8(self):
        self.assertEqual(check_email("test@.com."), "Invalid Email")

    def test_invalid_email9(self):
        self.assertEqual(check_email("test@.com."), "Invalid Email")

    def test_invalid_email10(self):
        self.assertEqual(check_email("test@.com."), "Invalid Email")
