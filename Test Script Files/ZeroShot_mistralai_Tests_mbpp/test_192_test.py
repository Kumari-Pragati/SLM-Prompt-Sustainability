import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_all_alphabets(self):
        self.assertTrue(check_String('abcdefghijklmnopqrstuvwxyz'))
        self.assertTrue(check_String('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self.assertTrue(check_String('AbCdEfGhIjKlMnOpQrStUvWxYz'))

    def test_all_numbers(self):
        self.assertTrue(check_String('1234567890'))
        self.assertTrue(check_String('123456789012'))
        self.assertTrue(check_String('12345678901234'))

    def test_mixed_alphanumeric(self):
        self.assertTrue(check_String('A1B2C3D4E5F6'))
        self.assertTrue(check_String('a1b2c3d4e5f6'))
        self.assertTrue(check_String('A1b2C3d4e5F6'))

    def test_invalid_string(self):
        self.assertFalse(check_String('!@#$%^&*()'))
        self.assertFalse(check_String('_ _ _ _ _'))
        self.assertFalse(check_String('abc!def'))
        self.assertFalse(check_String('1234567890123'))
