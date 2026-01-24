import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_single_uppercase_letter(self):
        self.assertEqual(count_char_position('A'), 1)
        self.assertEqual(count_char_position('Z'), 26)

    def test_single_lowercase_letter(self):
        self.assertEqual(count_char_position('a'), 1)
        self.assertEqual(count_char_position('z'), 26)

    def test_mixed_case_string(self):
        self.assertEqual(count_char_position('AbCdEfGhIjKlMnOpQrStUvWxYz'), 26)

    def test_string_with_non_alphabet_characters(self):
        self.assertEqual(count_char_position('A1B2C3'), 0)
        self.assertEqual(count_char_position('A!B@C#'), 0)
        self.assertEqual(count_char_position('A_B_C_'), 0)

    def test_string_with_only_numbers(self):
        self.assertEqual(count_char_position('1234567890'), 0)

    def test_string_with_only_special_characters(self):
        self.assertEqual(count_char_position('!@#$%^&*()_+-=[]{}|;:,.<>?'), 0)

    def test_string_with_whitespace(self):
        self.assertEqual(count_char_position(' A B C '), 0)

    def test_long_string(self):
        long_string = 'a' * 100 + 'A' * 100 + 'b' * 100 + 'B' * 100
        self.assertEqual(count_char_position(long_string), 520)
