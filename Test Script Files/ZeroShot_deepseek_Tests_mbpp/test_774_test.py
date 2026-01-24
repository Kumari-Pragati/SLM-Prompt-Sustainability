import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')
        self.assertEqual(check_email('test.email@example.co.uk'), 'Valid Email')
        self.assertEqual(check_email('test123@example.net'), 'Valid Email')

    def test_invalid_email(self):
        self.assertEqual(check_email('test@.com'), 'Invalid Email')
        self.assertEqual(check_email('test@example'), 'Invalid Email')
        self.assertEqual(check_email('test@.com'), 'Invalid Email')
        self.assertEqual(check_email('test@com'), 'Invalid Email')
        self.assertEqual(check_email('test@com.'), 'Invalid Email')
        self.assertEqual(check_email('test@.com.'), 'Invalid Email')
        self.assertEqual(check_email('test@com.c'), 'Invalid Email')
        self.assertEqual(check_email('test@com.co.'), 'Invalid Email')
        self.assertEqual(check_email('test@com.c.'), 'Invalid Email')
        self.assertEqual(check_email('test@com.co'), 'Invalid Email')
