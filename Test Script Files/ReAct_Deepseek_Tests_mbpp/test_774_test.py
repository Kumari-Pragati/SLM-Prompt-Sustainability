import unittest
from mbpp_774_code import check_email

class TestCheckEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertEqual(check_email('test@example.com'), 'Valid Email')
        self.assertEqual(check_email('test.email@domain.co.uk'), 'Valid Email')
        self.assertEqual(check_email('test123@subdomain.domain.info'), 'Valid Email')

    def test_invalid_email(self):
        self.assertEqual(check_email('test@.com'), 'Invalid Email')
        self.assertEqual(check_email('test@com'), 'Invalid Email')
        self.assertEqual(check_email('test@.com.'), 'Invalid Email')
        self.assertEqual(check_email('test@com.'), 'Invalid Email')
        self.assertEqual(check_email('test@domain..com'), 'Invalid Email')

    def test_empty_email(self):
        self.assertEqual(check_email(''), 'Invalid Email')

    def test_none_email(self):
        self.assertRaises(TypeError, check_email, None)
