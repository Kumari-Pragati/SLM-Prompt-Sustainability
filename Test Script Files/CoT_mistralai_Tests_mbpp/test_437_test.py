import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(remove_odd(char), char)

    def test_even_length_string(self):
        for string in ['aa', 'abcd', 'xyz', 'abcdefghijkl', '1234567890']:
            self.assertEqual(remove_odd(string), string[:len(string)//2])

    def test_odd_length_string(self):
        for string in ['a', 'abcd', 'xyz', 'abcdefghijklm', '12345678901']:
            self.assertEqual(remove_odd(string), string[:len(string)//2] + string[len(string)//2 + 1:])

    def test_string_with_only_odd_indexes(self):
        self.assertEqual(remove_odd('12345'), '135')

    def test_string_with_only_even_indexes(self):
        self.assertEqual(remove_odd('2468'), '2468')

    def test_string_with_mixed_even_and_odd_indexes(self):
        self.assertEqual(remove_odd('0123456789'), '02468')

    def test_string_with_non_alphanumeric_characters(self):
        self.assertEqual(remove_odd('!@#$%^&*()_+-=[]{}|;:,.<>?'), '!@#$%^&*()_+-=[]{}|;:,.<>')
