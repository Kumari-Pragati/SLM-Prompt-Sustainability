import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_minimum_length_with_single_letter(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_minimum_length_with_multiple_letters(self):
        self.assertEqual(minimum_Length('abc'), 1)

    def test_minimum_length_with_repeated_letters(self):
        self.assertEqual(minimum_Length('aaa'), 1)

    def test_minimum_length_with_multiple_repeated_letters(self):
        self.assertEqual(minimum_Length('aaaa'), 1)

    def test_minimum_length_with_longer_string(self):
        self.assertEqual(minimum_Length('abcdefghijklmnopqrstuvwxyz'), 1)

    def test_minimum_length_with_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_minimum_length_with_only_spaces(self):
        self.assertEqual(minimum_Length('   '), 1)

    def test_minimum_length_with_special_characters(self):
        self.assertEqual(minimum_Length('!@#$%^&*()_+-=[]{}|;:,.<>?'), 0)

    def test_minimum_length_with_numbers(self):
        self.assertEqual(minimum_Length('12345'), 5)
