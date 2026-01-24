import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):

    def test_upper_ctr_all_upper(self):
        self.assertEqual(upper_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_upper_ctr_all_lower(self):
        self.assertEqual(upper_ctr('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_upper_ctr_mixed(self):
        self.assertEqual(upper_ctr('AbCdEfGhIjKlMnOpQrStUvWxYz'), 13)

    def test_upper_ctr_empty(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_upper_ctr_numbers(self):
        self.assertEqual(upper_ctr('1234567890'), 0)

    def test_upper_ctr_special_chars(self):
        self.assertEqual(upper_ctr('!@#$%^&*()'), 0)
