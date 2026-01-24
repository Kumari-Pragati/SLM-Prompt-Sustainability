import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(''), (0, 0, 0))

    def test_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl('abcdefghijklmnopqrstuvwxyz'), (26, 0, 0))

    def test_all_digits(self):
        self.assertEqual(count_alpha_dig_spl('1234567890'), (0, 10, 0))

    def test_all_special_characters(self):
        self.assertEqual(count_alpha_dig_spl('!@#$%^&*()_+-=[]{}|;:,.<>?'), (0, 0, 22))

    def test_mixed_case_alphabets(self):
        self.assertEqual(count_alpha_dig_spl('ABCdefGHIJklMnOpQrSTuvWxYZ'), (26, 0, 0))

    def test_mixed_case_alphanumeric(self):
        self.assertEqual(count_alpha_dig_spl('A1b2C3d4E5f6'), (4, 2, 0))

    def test_mixed_special_characters(self):
        self.assertEqual(count_alpha_dig_spl('!@#$%^&*()_+-=[]{}|;:,.<>?'), (0, 0, 22))

    def test_string_with_only_special_characters(self):
        self.assertEqual(count_alpha_dig_spl('!@#$%^&*()_+-=[]{}|;:,.<>?'), (0, 0, 22))
