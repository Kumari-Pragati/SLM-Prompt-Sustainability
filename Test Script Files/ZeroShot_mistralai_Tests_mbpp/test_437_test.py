import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character_string(self):
        for char in ['a', 'b', 'c', 'd', 'e']:
            self.assertEqual(remove_odd(char), char)

    def test_even_length_string(self):
        for string in ['aa', 'ab', 'ba', 'bb', 'abc', 'cba', 'abcd', 'dcba']:
            self.assertEqual(remove_odd(string), string[::2])

    def test_odd_length_string(self):
        for string in ['a', 'ab', 'ac', 'ad', 'abc', 'bcd', 'bcda']:
            self.assertNotEqual(remove_odd(string), string)
