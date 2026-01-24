import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_only_digits(self):
        self.assertEqual(move_num('12345'), '12345')

    def test_only_letters(self):
        self.assertEqual(move_num('abcde'), 'abcde')

    def test_mixed_letters_and_digits(self):
        self.assertEqual(move_num('abc123def456'), 'abcdef123456')

    def test_leading_digits(self):
        self.assertEqual(move_num('1abcdef'), '1abcdef')

    def test_trailing_digits(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_digits_in_middle(self):
        self.assertEqual(move_num('abc123def'), 'abcdef123')

    def test_multiple_digit_groups(self):
        self.assertEqual(move_num('abc123def456ghi789'), 'abcdef456ghi789123')

    def test_single_digit(self):
        self.assertEqual(move_num('5'), '5')

    def test_long_string(self):
        self.assertEqual(move_num('a' * 100 + '1' * 100), 'a' * 100 + '1' * 100)

    def test_negative_numbers(self):
        self.assertEqual(move_num('-123'), '-123')

    def test_invalid_input(self):
        self.assertRaises(ValueError, move_num, 'abc!@#')
