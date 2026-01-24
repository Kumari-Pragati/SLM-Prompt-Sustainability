import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')
        self.assertEqual(check_email('test.test@example.com'), 'Valid Email')
        self.assertEqual(check_email('test.test@example.co.uk'), 'Valid Email')

    def test_invalid_email(self):
        self.assertEqual(check_email('test@.com'), 'Invalid Email')
        self.assertEqual(check_email('test@example'), 'Invalid Email')
        self.assertEqual(check_email('test@.com'), 'Invalid Email')
        self.assertEqual(check_email('test@com'), 'Invalid Email')
        self.assertEqual(check_email('test@com.'), 'Invalid Email')
        self.assertEqual(check_email('test@.com.'), 'Invalid Email')
        self.assertEqual(check_email('test@com.com'), 'Invalid Email')
        self.assertEqual(check_email('test@com.co.uk'), 'Invalid Email')

    def test_empty_string(self):
        self.assertEqual(check_email(''), 'Invalid Email')

    def test_none(self):
        with self.assertRaises(TypeError):
            check_email(None)
