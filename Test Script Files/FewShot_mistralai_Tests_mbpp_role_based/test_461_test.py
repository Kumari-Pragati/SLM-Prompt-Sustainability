import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_all_uppercase(self):
        self.assertEqual(upper_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_all_lowercase(self):
        self.assertEqual(upper_ctr('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr('AbCdEfGhIjKlMnOpQrStUvWxYz'), 10)

    def test_single_uppercase(self):
        self.assertEqual(upper_ctr('A'), 1)

    def test_single_lowercase(self):
        self.assertEqual(upper_ctr('a'), 0)
