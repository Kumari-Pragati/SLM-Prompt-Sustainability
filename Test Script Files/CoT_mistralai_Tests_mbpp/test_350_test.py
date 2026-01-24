import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_single_letter(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(minimum_Length(char), 1)

    def test_multiple_letters(self):
        for letters in ['aaa', 'abcd', 'xyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
            self.assertEqual(minimum_Length(letters), 1)

    def test_longer_strings(self):
        for letters in ['aaaaaaa', 'abababab', 'xyzxyzxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']:
            self.assertEqual(minimum_Length(letters), len(letters) - 1)

    def test_mixed_case(self):
        for letters in ['AaBbCc', 'aAbBcC', 'AbBcCdD', 'aAbBcCdDeE']:
            self.assertEqual(minimum_Length(letters), 1)

    def test_special_characters(self):
        for letters in ['!@#$%^&*()_+-=', 'abcdefghijklmnopqrstuvwxyz1234567890', 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=']:
            self.assertRaises(ValueError, minimum_Length, letters)
