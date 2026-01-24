import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(''), (0, 0, 0))

    def test_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl('abcdefghijklmnopqrstuvwxyz'), (26, 0, 0))

    def test_all_digits(self):
        self.assertEqual(count_alpha_dig_spl('1234567890'), (0, 10, 0))

    def test_mixed_case(self):
        self.assertEqual(count_alpha_dig_spl('AbCdEfGhIjKlMnOpQrStUvWxYz1234567890!@#$%^&*()'), (26, 10, 3))

    def test_special_characters(self):
        self.assertEqual(count_alpha_dig_spl('!@#$%^&*()'), (0, 0, 8))

    def test_empty_characters(self):
        self.assertEqual(count_alpha_dig_spl('  '), (0, 0, 3))
