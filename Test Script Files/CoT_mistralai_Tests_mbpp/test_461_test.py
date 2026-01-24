import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(upper_ctr(''), 0)

    def test_all_uppercase(self):
        self.assertEqual(upper_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr('AbCdEfGhIjKlMnOpQrStUvWxYz'), 26)

    def test_single_uppercase(self):
        self.assertEqual(upper_ctr('A'), 1)

    def test_single_lowercase(self):
        self.assertEqual(upper_ctr('a'), 0)

    def test_special_characters(self):
        self.assertEqual(upper_ctr('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            upper_ctr([])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            upper_ctr(123)
