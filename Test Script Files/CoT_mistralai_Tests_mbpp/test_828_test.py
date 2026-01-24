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
        self.assertEqual(count_alpha_dig_spl('ABC123def456'), (3, 3, 3))

    def test_special_characters(self):
        self.assertEqual(count_alpha_dig_spl('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), (0, 0, 12))

    def test_single_char(self):
        for char in 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:'\'<>,.?/':
            self.assertEqual(count_alpha_dig_spl(char), (1, 0, 0 if char.isalpha() else 0, 0 if char.isdigit() else 1))

    def test_long_string(self):
        long_string = 'a' * 100 + '1' * 100 + '!' * 100
        self.assertEqual(count_alpha_dig_spl(long_string), (100, 100, 100))
